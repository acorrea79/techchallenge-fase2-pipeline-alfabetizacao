"""
Ingestão Batch da pipeline.

Responsável por representar a extração das tabelas públicas da Base dos Dados
via BigQuery Sandbox e gravação na camada Bronze.
"""


SMALL_TABLES = [
    "meta_alfabetizacao_brasil",
    "meta_alfabetizacao_uf",
    "meta_alfabetizacao_municipio",
    "municipio",
    "uf",
    "dicionario",
]


def build_select_all_query(table_id: str) -> str:
    return f"SELECT * FROM `{table_id}`"


def build_alunos_sample_query(table_id: str, limit: int = 100000) -> str:
    return f"""
    SELECT
      ano,
      id_municipio,
      id_escola,
      id_aluno,
      caderno,
      serie,
      rede,
      presenca,
      preenchimento_caderno,
      alfabetizado,
      proficiencia,
      peso_aluno
    FROM `{table_id}`
    LIMIT {limit}
    """


def build_alunos_aggregated_query(table_id: str) -> str:
    return f"""
    SELECT
      ano,
      id_municipio,
      rede,
      serie,
      COUNT(*) AS total_alunos,
      COUNTIF(proficiencia IS NOT NULL) AS total_com_proficiencia,
      AVG(proficiencia) AS media_proficiencia,
      MIN(proficiencia) AS menor_proficiencia,
      MAX(proficiencia) AS maior_proficiencia,
      COUNTIF(alfabetizado IS NOT NULL) AS total_com_status_alfabetizacao,
      COUNT(DISTINCT alfabetizado) AS qtd_status_alfabetizacao,
      COUNTIF(presenca IS NOT NULL) AS total_com_status_presenca,
      AVG(peso_aluno) AS media_peso_aluno
    FROM `{table_id}`
    GROUP BY ano, id_municipio, rede, serie
    """
