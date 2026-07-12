
# Evidências Cloud / BigQuery

## 1. Objetivo

Este documento registra as evidências de uso de ambiente cloud no projeto **TechChallenge Fase 2 — Pipeline Híbrido para Análise da Alfabetização no Brasil**.

A solução utiliza o **Google Cloud BigQuery Sandbox** como fonte cloud real para consulta dos dados públicos da Base dos Dados.

## 2. Projeto GCP utilizado

- Projeto GCP: `fiap-techchallenge-fase2`
- Dataset público: `basedosdados.br_inep_avaliacao_alfabetizacao`
- Ambiente de execução: Google Colab
- Linguagem principal: Python
- Motor de consulta cloud: BigQuery

## 3. Tabelas públicas consultadas

As tabelas utilizadas pertencem ao dataset público da Base dos Dados:

| table_name                   |   total_rows |   size_mb |
|:-----------------------------|-------------:|----------:|
| alunos                       |      3867999 |    256.1  |
| municipio                    |        23995 |      1.75 |
| meta_alfabetizacao_municipio |        10704 |      1.1  |
| uf                           |          145 |      0.01 |
| meta_alfabetizacao_uf        |           81 |      0.01 |
| dicionario                   |           27 |      0    |
| meta_alfabetizacao_brasil    |            3 |      0    |

## 4. Papel do BigQuery na arquitetura

O BigQuery foi utilizado para:

- localizar o dataset público;
- consultar metadados das tabelas;
- validar estrutura das entidades obrigatórias;
- estimar volume das tabelas;
- executar consultas de ingestão batch;
- gerar amostra controlada da tabela `alunos`;
- gerar visão agregada da tabela `alunos`.

## 5. Estratégia adotada

A tabela `alunos` possui maior volume. Por isso, foram adotadas duas estratégias:

1. amostra controlada de 100.000 linhas;
2. agregação por ano, município, rede e série.

Essa decisão reduz custo, evita processamento desnecessário e mantém informação suficiente para análise educacional.

## 6. Evidência de bytes processados

As principais consultas foram avaliadas com `dry_run` do BigQuery, sem executar novamente a leitura dos dados.

| description                                       |   mb_processed |   gb_processed |   percent_of_monthly_free_tier |
|:--------------------------------------------------|---------------:|---------------:|-------------------------------:|
| Listagem das tabelas do dataset público           |         0      |       0        |                       0        |
| Ingestão integral meta_alfabetizacao_brasil       |         0.0003 |       0        |                       0        |
| Ingestão integral meta_alfabetizacao_uf           |         0.007  |       7e-06    |                       1e-06    |
| Ingestão integral meta_alfabetizacao_municipio    |         1.0979 |       0.001072 |                       0.000105 |
| Ingestão integral municipio                       |         1.7472 |       0.001706 |                       0.000167 |
| Ingestão integral uf                              |         0.0099 |       1e-05    |                       1e-06    |
| Ingestão integral dicionario                      |         0.0011 |       1e-06    |                       0        |
| Amostra controlada alunos LIMIT 100000            |       256.105  |       0.250102 |                       0.024424 |
| Agregação alunos por ano, município, rede e série |       158.164  |       0.154457 |                       0.015084 |

## 7. Evolução produtiva possível

Em uma arquitetura produtiva, a solução poderia evoluir para:

- Cloud Storage como armazenamento Bronze/Silver/Gold;
- BigQuery Tables para materialização analítica;
- Pub/Sub para ingestão streaming real;
- Dataflow para processamento streaming escalável;
- Cloud Monitoring para alertas operacionais;
- Vertex AI ou BigQuery ML para modelos preditivos.

## 8. Conclusão

O projeto demonstra uso real de cloud por meio do BigQuery Sandbox e mantém a execução acadêmica compatível com a restrição de custo zero.
