# Arquitetura da Solução

## Visão Geral

A arquitetura utiliza BigQuery Sandbox como fonte cloud, Google Colab como ambiente de execução e arquivos CSV, JSONL e Parquet para materialização das camadas.

```mermaid
flowchart TD
    A[Base dos Dados / BigQuery Sandbox] --> B[Google Colab / Python]
    B --> C[Bronze Batch - CSV]
    B --> D[Bronze Streaming - JSONL]
    C --> E[Silver - Parquet]
    D --> F[Silver Streaming - Parquet]
    E --> G[Gold - Parquet]
    F --> H[Gold Streaming - Parquet]
    G --> I[Qualidade Consolidada]
    H --> I
    I --> J[Monitoramento Consolidado]
    J --> K[README / Docs / Evidências]
```

## Fluxo Batch

```mermaid
flowchart LR
    A[BigQuery Público] --> B[Ingestão Batch]
    B --> C[Bronze CSV]
    C --> D[Tratamento Silver]
    D --> E[Silver Parquet]
    E --> F[Gold Analytics]
    F --> G[Datasets Analíticos]
```

## Fluxo Streaming

```mermaid
flowchart LR
    A[Producer Python] --> B[Eventos JSONL]
    B --> C[Bronze Streaming]
    C --> D[Consumer Micro-batch]
    D --> E{Validação}
    E -->|Eventos válidos| F[Silver Streaming]
    E -->|Eventos inválidos| G[Quarentena]
    F --> H[Gold Streaming]
    H --> I[Monitoramento]
```

## Camadas

- Bronze: dados brutos e eventos originais.
- Silver: dados padronizados e validados.
- Gold: bases analíticas finais.
- Quality: validação consolidada.
- Monitoring: observabilidade e status executivo.
