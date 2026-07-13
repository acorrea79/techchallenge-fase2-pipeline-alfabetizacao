"""
Monitoramento consolidado da pipeline.

Funções para criar registros, alertas e resumo executivo.
"""

from datetime import datetime


def create_record(component: str, layer: str, status: str, details: dict | None = None) -> dict:
    return {
        "execution_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "component": component,
        "layer": layer,
        "status": status,
        "details": details or {},
    }


def create_alert(severity: str, component: str, message: str, details: dict | None = None) -> dict:
    return {
        "execution_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "severity": severity,
        "component": component,
        "message": message,
        "details": details or {},
    }


def calculate_status(records: list[dict], alerts: list[dict]) -> str:
    failed = sum(1 for item in records if item.get("status") == "failed")
    critical = sum(1 for item in alerts if item.get("severity") == "critical")
    warning = sum(1 for item in alerts if item.get("severity") == "warning")

    if failed > 0 or critical > 0:
        return "failed"

    if warning > 0:
        return "approved_with_warnings"

    return "approved"
