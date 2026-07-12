
# Estratégia FinOps

## 1. Objetivo

Este documento descreve as decisões de controle de custo adotadas no projeto.

O projeto foi desenvolvido sob a restrição acadêmica de **custo zero**, utilizando BigQuery Sandbox, Google Colab e armazenamento local/reprodutível em arquivos.

## 2. Estratégias de controle de custo

As principais estratégias FinOps adotadas foram:

### 2.1 Uso do BigQuery Sandbox

O BigQuery Sandbox permitiu consultar os dados públicos sem ativar billing no projeto.

### 2.2 Controle da tabela `alunos`

A tabela `alunos` é a maior fonte do dataset. Para evitar leitura desnecessária, a pipeline não materializa a tabela completa na Bronze.

Foram geradas:

- `alunos_sample.csv`: amostra controlada;
- `alunos_agregado.csv`: visão agregada por ano, município, rede e série.

### 2.3 Seleção explícita de colunas

Nas consultas maiores, a pipeline seleciona apenas as colunas necessárias, evitando leitura excessiva.

### 2.4 Uso de Parquet

As camadas Silver e Gold são salvas em Parquet, formato colunar mais eficiente para leitura analítica e armazenamento.

### 2.5 Micro-batches no streaming simulado

O streaming foi implementado em micro-batches, permitindo controlar volume, latência e tratamento de eventos inválidos.

### 2.6 Dry run para estimativa de processamento

As principais consultas foram avaliadas usando `dry_run`, permitindo estimar bytes processados antes da execução.

## 3. Estimativa consolidada

- Bytes estimados nas consultas avaliadas: `437394228`
- GB estimados: `0.407355`
- Percentual estimado do limite mensal gratuito de 1 TiB: `0.039781%`

## 4. Decisões arquiteturais

A solução não materializa todas as camadas em BigQuery para evitar risco de custo, billing e dependências de serviços pagos.

Em vez disso, usa:

- BigQuery como fonte cloud;
- Colab como motor de execução;
- CSV na Bronze;
- Parquet na Silver e Gold;
- JSONL no streaming;
- manifestos e relatórios para rastreabilidade.

## 5. Trade-offs

### Vantagens

- custo zero;
- simples reprodução acadêmica;
- baixo risco operacional;
- arquitetura clara;
- dados analíticos em Parquet;
- controle de volume.

### Limitações

- não há ingestão streaming real com Pub/Sub;
- não há Dataflow;
- não há materialização permanente em BigQuery;
- arquivos gerados no Colab precisam ser reproduzidos pela execução do notebook.

## 6. Evolução futura

Em ambiente produtivo, a arquitetura poderia incluir:

- Cloud Storage para armazenamento das camadas;
- BigQuery para materialização Gold;
- Pub/Sub para eventos em tempo real;
- Dataflow para streaming;
- Cloud Composer para orquestração;
- Cloud Monitoring para alertas;
- BigQuery ML ou Vertex AI para modelos preditivos.

## 7. Conclusão

A solução atende ao objetivo acadêmico com controle de custo, rastreabilidade e uso real de cloud, mantendo compatibilidade com a restrição de não ativar billing.
