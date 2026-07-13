"""
Transformações da camada Silver.

Contém funções de limpeza, padronização, tipagem e remoção de duplicidades.
"""

from datetime import datetime
import pandas as pd


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df


def normalize_keys(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "id_municipio" in df.columns:
        df["id_municipio"] = (
            df["id_municipio"].astype("string")
            .str.replace(r"\.0$", "", regex=True)
            .str.zfill(7)
        )

    if "sigla_uf" in df.columns:
        df["sigla_uf"] = df["sigla_uf"].astype("string").str.upper().str.strip()

    if "rede" in df.columns:
        df["rede"] = df["rede"].astype("string").str.replace(r"\.0$", "", regex=True).str.strip()

    if "serie" in df.columns:
        df["serie"] = df["serie"].astype("string").str.replace(r"\.0$", "", regex=True).str.strip()

    return df


def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    integer_columns = [
        "ano",
        "nivel_alfabetizacao",
        "total_alunos",
        "total_com_proficiencia",
        "total_com_status_alfabetizacao",
        "qtd_status_alfabetizacao",
        "total_com_status_presenca",
    ]

    float_prefixes = [
        "taxa_",
        "meta_",
        "percentual_",
        "media_",
        "proporcao_",
        "proficiencia",
        "peso_",
        "menor_",
        "maior_",
    ]

    for column in integer_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce").astype("Int64")

    for column in df.columns:
        if any(column.startswith(prefix) for prefix in float_prefixes):
            df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def remove_duplicates(df: pd.DataFrame, keys: list | None = None):
    df = df.copy()
    before = len(df)
    if keys:
        available = [column for column in keys if column in df.columns]
        df = df.drop_duplicates(subset=available)
    else:
        df = df.drop_duplicates()
    return df, before - len(df)


def add_metadata(df: pd.DataFrame, source_table: str) -> pd.DataFrame:
    df = df.copy()
    df["source_table"] = source_table
    df["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df["layer"] = "silver"
    return df
