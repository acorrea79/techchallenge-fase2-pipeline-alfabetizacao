"""
Utilitários de arquivos para a pipeline.
"""

from pathlib import Path
import json
import pandas as pd


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_json(data, path: Path) -> Path:
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return path


def read_json(path: Path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_csv(df: pd.DataFrame, path: Path) -> Path:
    ensure_dir(path.parent)
    df.to_csv(path, index=False, encoding="utf-8")
    return path


def save_parquet(df: pd.DataFrame, path: Path) -> Path:
    ensure_dir(path.parent)
    df.to_parquet(path, index=False)
    return path
