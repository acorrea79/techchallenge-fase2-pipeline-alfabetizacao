
-- TechChallenge Fase 2
-- Consultas BigQuery / FinOps
-- Dataset público: basedosdados.br_inep_avaliacao_alfabetizacao

-- 1. Volume das tabelas públicas
SELECT
  table_id AS table_name,
  row_count AS total_rows,
  ROUND(size_bytes / 1024 / 1024, 2) AS size_mb
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.__TABLES__`
ORDER BY
  size_bytes DESC;

-- 2. Consulta controlada da tabela alunos
-- Estratégia FinOps: limitar amostra para evitar leitura desnecessária.
SELECT
  ano,
  id_municipio,
  id_escola,
  id_aluno,
  serie,
  rede,
  presenca,
  alfabetizado,
  proficiencia,
  peso_aluno
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.alunos`
LIMIT 100000;

-- 3. Consulta agregada da tabela alunos
-- Estratégia FinOps: reduzir granularidade para análise municipal.
SELECT
  ano,
  id_municipio,
  rede,
  serie,
  COUNT(*) AS total_alunos,
  AVG(proficiencia) AS media_proficiencia,
  AVG(peso_aluno) AS media_peso_aluno
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.alunos`
GROUP BY
  ano,
  id_municipio,
  rede,
  serie;

-- 4. Exemplo de consulta com seleção explícita de colunas
-- Estratégia FinOps: evitar SELECT * em tabelas grandes.
SELECT
  ano,
  id_municipio,
  rede,
  serie,
  taxa_alfabetizacao,
  media_portugues
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.municipio`;
