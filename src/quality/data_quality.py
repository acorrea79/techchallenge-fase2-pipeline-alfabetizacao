"""
Qualidade de dados.

Funções reutilizáveis para validação de colunas, nulos, duplicidades e percentuais.
"""

import pandas as pd


def status_from_issue_count(issue_count: int, warning_allowed: bool = False) -> str:
    if issue_count == 0:
        return "approved"
    if warning_allowed:
        return "warning"
    return "failed"


def validate_required_columns(df: pd.DataFrame, required_columns: list) -> tuple[str, list]:
    missing = [column for column in required_columns if column not in df.columns]
    return ("approved" if not missing else "failed"), missing


def validate_required_not_null(df: pd.DataFrame, required_columns: list) -> tuple[str, dict]:
    nulls = {}

    for column in required_columns:
        if column in df.columns:
            count = int(df[column].isna().sum())
            if count > 0:
                nulls[column] = count

    return status_from_issue_count(sum(nulls.values())), nulls


def validate_duplicates(df: pd.DataFrame, keys: list) -> tuple[str, int]:
    available = [column for column in keys if column in df.columns]

    if not available:
        return "warning", 0

    count = int(df.duplicated(subset=available).sum())
    return status_from_issue_count(count), count


def validate_percentage_range(df: pd.DataFrame) -> tuple[str, dict]:
    columns = [
        column for column in df.columns
        if column.startswith("taxa_")
        or column.startswith("meta_")
        or column.startswith("percentual_")
        or column.startswith("proporcao_")
    ]

    invalids = {}

    for column in columns:
        values = pd.to_numeric(df[column], errors="coerce")
        count = int(((values < 0) | (values > 100)).sum())
        if count > 0:
            invalids[column] = count

    return status_from_issue_count(sum(invalids.values())), invalids
