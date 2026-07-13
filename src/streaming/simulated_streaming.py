"""
Streaming simulado.

Gera, grava, lê e valida eventos em JSONL para micro-batches.
"""

from datetime import datetime, timedelta
from pathlib import Path
import json
import random
import uuid
import numpy as np
import pandas as pd


ALLOWED_EVENT_TYPES = [
    "atualizacao_indicador",
    "nova_medicao_desempenho",
    "atualizacao_meta_resultado",
]

REQUIRED_FIELDS = [
    "event_id",
    "event_timestamp",
    "event_type",
    "ano",
    "id_municipio",
    "rede",
    "serie",
    "taxa_alfabetizacao_evento",
]


def safe_json_value(value):
    if pd.isna(value):
        return None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def generate_event(row: pd.Series) -> dict:
    taxa = max(0, min(100, float(row["taxa_alfabetizacao"]) + random.uniform(-3, 3)))

    return {
        "event_id": str(uuid.uuid4()),
        "event_timestamp": (datetime.now() - timedelta(seconds=random.randint(1, 300))).strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": random.choice(ALLOWED_EVENT_TYPES),
        "source_system": "simulador_python_colab",
        "ano": int(row["ano"]),
        "id_municipio": str(row["id_municipio"]).zfill(7),
        "sigla_uf": safe_json_value(row.get("sigla_uf")),
        "rede": safe_json_value(row.get("rede")),
        "serie": safe_json_value(row.get("serie")),
        "taxa_alfabetizacao_evento": round(taxa, 4),
        "meta_referencia_evento": safe_json_value(row.get("meta_referencia")),
    }


def write_jsonl(events: list[dict], output_file: Path) -> Path:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        for event in events:
            file.write(json.dumps(event, ensure_ascii=False) + "\n")
    return output_file


def read_jsonl(file_path: Path) -> pd.DataFrame:
    with open(file_path, "r", encoding="utf-8") as file:
        return pd.DataFrame(json.loads(line) for line in file)


def validate_event(row, seen_event_ids: set) -> list:
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in row or pd.isna(row[field]) or row[field] == "":
            errors.append(f"campo_obrigatorio_ausente:{field}")

    if row.get("event_id") in seen_event_ids:
        errors.append("evento_duplicado:event_id")
    else:
        seen_event_ids.add(row.get("event_id"))

    if row.get("event_type") not in ALLOWED_EVENT_TYPES:
        errors.append("event_type_invalido")

    try:
        taxa = float(row.get("taxa_alfabetizacao_evento"))
        if taxa < 0 or taxa > 100:
            errors.append("taxa_alfabetizacao_fora_faixa_0_100")
    except Exception:
        errors.append("taxa_alfabetizacao_nao_numerica")

    return errors
