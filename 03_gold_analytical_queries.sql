
-- TechChallenge Fase 2
-- Consultas analíticas representativas para a camada Gold
-- Observação: no projeto acadêmico, a Gold foi materializada em Parquet via Colab.
-- Em uma evolução produtiva, estes datasets poderiam ser materializados em BigQuery.

-- 1. Municípios com menor taxa de alfabetização
SELECT
  ano,
  id_municipio,
  sigla_uf,
  rede,
  serie,
  taxa_alfabetizacao,
  meta_referencia,
  distancia_meta_pontos,
  status_meta
FROM gold_comparativo_meta_resultado_municipio
ORDER BY
  taxa_alfabetizacao ASC;

-- 2. Ranking de municípios prioritários
SELECT
  ano,
  id_municipio,
  sigla_uf,
  rede,
  taxa_alfabetizacao,
  score_prioridade,
  ranking_prioridade,
  criterio_priorizacao
FROM gold_ranking_municipios_prioritarios
ORDER BY
  ano,
  rede,
  ranking_prioridade;

-- 3. Evolução temporal por UF e rede
SELECT
  ano,
  sigla_uf,
  rede,
  serie,
  taxa_alfabetizacao,
  variacao_taxa_alfabetizacao,
  status_meta
FROM gold_evolucao_alfabetizacao_uf
ORDER BY
  sigla_uf,
  rede,
  serie,
  ano;

-- 4. Base preparada para IA
SELECT
  ano,
  id_municipio,
  sigla_uf,
  rede,
  serie,
  taxa_alfabetizacao,
  media_portugues,
  total_alunos,
  media_proficiencia,
  meta_referencia,
  distancia_meta_pontos,
  status_meta
FROM gold_base_ia_alfabetizacao;
