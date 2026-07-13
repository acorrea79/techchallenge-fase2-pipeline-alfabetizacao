"""
Transformações da camada Gold.

Contém funções para integração analítica, metas, UF e ranking de prioridade.
"""

from datetime import datetime
import numpy as np
import pandas as pd


UF_CODE_TO_SIGLA = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO",
    "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL", "28": "SE", "29": "BA",
    "31": "MG", "32": "ES", "33": "RJ", "35": "SP",
    "41": "PR", "42": "SC", "43": "RS",
    "50": "MS", "51": "MT", "52": "GO", "53": "DF",
}


def derive_sigla_uf_from_municipio(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["id_municipio"] = df["id_municipio"].astype("string").str.zfill(7)
    df["id_uf"] = df["id_municipio"].str[:2]
    df["sigla_uf"] = df["id_uf"].map(UF_CODE_TO_SIGLA).astype("string")
    return df


def add_meta_reference(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    def reference_year(ano):
        if pd.isna(ano):
            return pd.NA
        ano = int(ano)
        if ano < 2024:
            return 2024
        if ano > 2030:
            return 2030
        return ano

    df["ano_meta_referencia"] = df["ano"].apply(reference_year).astype("Int64")
    df["meta_referencia"] = np.nan

    for year in range(2024, 2031):
        column = f"meta_alfabetizacao_{year}"
        if column in df.columns:
            df.loc[df["ano_meta_referencia"] == year, "meta_referencia"] = df[column]

    df["distancia_meta_pontos"] = df["taxa_alfabetizacao"] - df["meta_referencia"]

    df["status_meta"] = np.select(
        [
            df["meta_referencia"].isna(),
            df["distancia_meta_pontos"] >= 0,
            df["distancia_meta_pontos"] < 0,
        ],
        [
            "sem_meta_referencia",
            "atingiu_ou_superou_meta",
            "abaixo_da_meta",
        ],
        default="indefinido",
    )

    if "meta_alfabetizacao_2030" in df.columns:
        df["distancia_meta_2030_pontos"] = df["taxa_alfabetizacao"] - df["meta_alfabetizacao_2030"]

    return df


def create_priority_ranking(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for column in ["taxa_alfabetizacao", "distancia_meta_pontos", "distancia_meta_2030_pontos"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    df["gap_meta_referencia"] = np.where(
        df["distancia_meta_pontos"] < 0,
        df["distancia_meta_pontos"].abs(),
        0,
    )

    df["gap_meta_2030"] = np.where(
        df["distancia_meta_2030_pontos"] < 0,
        df["distancia_meta_2030_pontos"].abs(),
        0,
    )

    df["gap_taxa_alfabetizacao"] = (100 - df["taxa_alfabetizacao"]).clip(lower=0)

    df["score_prioridade"] = (
        df["gap_meta_referencia"].fillna(0) * 0.50
        + df["gap_meta_2030"].fillna(0) * 0.30
        + df["gap_taxa_alfabetizacao"].fillna(0) * 0.20
    )

    below_target = df[df["status_meta"] == "abaixo_da_meta"].copy()

    if len(below_target) > 0:
        ranking = below_target
        ranking["criterio_priorizacao"] = "abaixo_da_meta_referencia"
    else:
        ranking = df[df["taxa_alfabetizacao"].notna()].copy()
        ranking["criterio_priorizacao"] = "fallback_menor_taxa_e_distancia_meta_2030"

    ranking = ranking.sort_values(["ano", "rede", "score_prioridade"], ascending=[True, True, False])
    ranking["ranking_prioridade"] = (
        ranking.groupby(["ano", "rede"])["score_prioridade"]
        .rank(method="dense", ascending=False)
        .astype("Int64")
    )

    ranking["gold_dataset"] = "gold_ranking_municipios_prioritarios"
    ranking["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ranking["layer"] = "gold"

    return ranking
