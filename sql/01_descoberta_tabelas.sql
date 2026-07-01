-- ============================================================================
-- 01_descoberta_tabelas.sql
-- ============================================================================
-- Projeto: TechChallenge Fase 2 - Pipeline Híbrido para Análise da Alfabetização no Brasil
-- Integrante: Andre Correa Luis Vilas Boas
-- Instituição: FIAP
-- Turma: 1IAST
--
-- Objetivo:
-- Registrar as consultas utilizadas para descoberta, validação inicial e
-- entendimento das tabelas do dataset principal do projeto.
--
-- Fonte principal:
-- Base dos Dados / INEP / Avaliação da Alfabetização
--
-- Dataset principal:
-- basedosdados.br_inep_avaliacao_alfabetizacao
--
-- Ambiente:
-- BigQuery Sandbox, sem ativação de billing.
--
-- Observação:
-- As consultas usam LIMIT quando aplicável para reduzir consumo de processamento.
-- ============================================================================


-- ============================================================================
-- 1. Consulta de teste para validar acesso ao BigQuery
-- ============================================================================

SELECT
  'BigQuery Sandbox acessado com sucesso' AS status;


-- ============================================================================
-- 2. Listagem das tabelas disponíveis no dataset principal
-- ============================================================================

SELECT
  table_catalog,
  table_schema,
  table_name,
  table_type
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.INFORMATION_SCHEMA.TABLES`
ORDER BY
  table_name;


-- ============================================================================
-- 3. Listagem das colunas das tabelas do dataset principal
-- ============================================================================

SELECT
  table_name,
  column_name,
  data_type,
  is_nullable,
  ordinal_position
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.INFORMATION_SCHEMA.COLUMNS`
ORDER BY
  table_name,
  ordinal_position;


-- ============================================================================
-- 4. Volume das tabelas
-- Objetivo:
-- Identificar tamanho e quantidade de linhas para apoiar decisões de FinOps,
-- principalmente sobre a tabela alunos.
-- ============================================================================

SELECT
  table_name,
  total_rows,
  ROUND(total_logical_bytes / 1024 / 1024, 2) AS tamanho_mb
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.INFORMATION_SCHEMA.TABLE_STORAGE`
ORDER BY
  total_logical_bytes DESC;


-- ============================================================================
-- 5. Perfil básico das tabelas alunos e municipio
-- Objetivo:
-- Verificar quantidade de anos, municípios, redes e séries disponíveis.
-- ============================================================================

SELECT
  'alunos' AS tabela,
  COUNT(*) AS total_linhas,
  COUNT(DISTINCT ano) AS qtd_anos,
  COUNT(DISTINCT id_municipio) AS qtd_municipios,
  COUNT(DISTINCT rede) AS qtd_redes,
  COUNT(DISTINCT serie) AS qtd_series
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.alunos`

UNION ALL

SELECT
  'municipio' AS tabela,
  COUNT(*) AS total_linhas,
  COUNT(DISTINCT ano) AS qtd_anos,
  COUNT(DISTINCT id_municipio) AS qtd_municipios,
  COUNT(DISTINCT rede) AS qtd_redes,
  COUNT(DISTINCT serie) AS qtd_series
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.municipio`;


-- ============================================================================
-- 6. Valores distintos de ano, rede e série na tabela municipio
-- Objetivo:
-- Entender os recortes disponíveis para análise.
-- ============================================================================

SELECT DISTINCT
  ano,
  rede,
  serie
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.municipio`
ORDER BY
  ano,
  rede,
  serie;


-- ============================================================================
-- 7. Consulta ao dicionário de dados
-- Objetivo:
-- Identificar o significado dos códigos utilizados nas tabelas,
-- como rede, presença, alfabetizado e nível de alfabetização.
-- ============================================================================

SELECT
  id_tabela,
  nome_coluna,
  chave,
  cobertura_temporal,
  valor
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.dicionario`
ORDER BY
  id_tabela,
  nome_coluna,
  chave;


-- ============================================================================
-- 8. Amostras das tabelas principais
-- Objetivo:
-- Visualizar estrutura e conteúdo inicial das tabelas.
-- Usar LIMIT para evitar consumo desnecessário.
-- ============================================================================

SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.alunos`
LIMIT 10;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_brasil`
LIMIT 10;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_uf`
LIMIT 10;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_municipio`
LIMIT 10;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.municipio`
LIMIT 10;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.uf`
LIMIT 10;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.dicionario`
LIMIT 50;


-- ============================================================================
-- 9. Consulta de apoio para ingestão batch das tabelas pequenas
-- Objetivo:
-- Estas tabelas podem ser ingeridas integralmente no pipeline acadêmico,
-- pois possuem baixo volume.
-- ============================================================================

SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_brasil`;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_uf`;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_municipio`;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.municipio`;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.uf`;


SELECT *
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.dicionario`;


-- ============================================================================
-- 10. Consulta controlada da tabela alunos
-- Objetivo:
-- A tabela alunos possui maior volume. Para manter o projeto em custo zero,
-- a ingestão inicial será feita de forma controlada.
--
-- Estratégia:
-- Usar amostra limitada para demonstração da pipeline.
-- Em cenário produtivo, a carga poderia ser completa ou particionada por ano,
-- UF, município ou outro critério.
-- ============================================================================

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
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.alunos`
LIMIT 100000;


-- ============================================================================
-- 11. Consulta agregada da tabela alunos
-- Objetivo:
-- Gerar uma visão mais leve para análise, agrupando dados por ano, município,
-- rede e série.
-- ============================================================================

SELECT
  ano,
  id_municipio,
  rede,
  serie,
  COUNT(*) AS total_alunos,
  COUNTIF(alfabetizado IS NOT NULL) AS total_com_status_alfabetizacao,
  AVG(proficiencia) AS media_proficiencia,
  AVG(peso_aluno) AS media_peso_aluno
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.alunos`
GROUP BY
  ano,
  id_municipio,
  rede,
  serie
ORDER BY
  ano,
  id_municipio,
  rede,
  serie;


-- ============================================================================
-- 12. Consulta de apoio para comparação entre resultado municipal e meta
-- Objetivo:
-- Validar campos que futuramente serão usados na camada Gold.
-- ============================================================================

SELECT
  m.ano,
  m.id_municipio,
  m.rede,
  m.serie,
  m.taxa_alfabetizacao,
  mm.meta_alfabetizacao_2024,
  mm.meta_alfabetizacao_2025,
  mm.meta_alfabetizacao_2026,
  mm.meta_alfabetizacao_2027,
  mm.meta_alfabetizacao_2028,
  mm.meta_alfabetizacao_2029,
  mm.meta_alfabetizacao_2030,
  mm.nivel_alfabetizacao,
  mm.percentual_participacao
FROM
  `basedosdados.br_inep_avaliacao_alfabetizacao.municipio` AS m
LEFT JOIN
  `basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_municipio` AS mm
ON
  m.ano = mm.ano
  AND m.id_municipio = mm.id_municipio
  AND m.rede = mm.rede
LIMIT 100;