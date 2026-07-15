# Organização do Código-Fonte

## Objetivo

Este documento descreve a organização dos scripts Python do projeto.

O notebook `notebooks/pipeline_alfabetizacao.ipynb` permanece como fluxo principal de execução no Google Colab. A pasta `src/` organiza as responsabilidades da pipeline em módulos reutilizáveis.

## Estrutura

```text
src/
├── ingestion/
│   └── batch_ingestion.py
├── processing/
│   ├── silver_transform.py
│   └── gold_transform.py
├── streaming/
│   └── simulated_streaming.py
├── quality/
│   └── data_quality.py
├── monitoring/
│   └── pipeline_monitoring.py
└── utils/
    └── file_utils.py
```

## Responsabilidades

- `src/ingestion/batch_ingestion.py`: consultas e lógica da ingestão Batch.
- `src/processing/silver_transform.py`: limpeza, padronização e transformação para Silver.
- `src/processing/gold_transform.py`: integrações analíticas e ranking de prioridade.
- `src/streaming/simulated_streaming.py`: simulação, gravação, leitura e validação de eventos.
- `src/quality/data_quality.py`: validações de qualidade.
- `src/monitoring/pipeline_monitoring.py`: registros e status de monitoramento.
- `src/utils/file_utils.py`: utilitários de arquivos.

## Decisão arquitetural

O projeto utiliza o notebook como execução principal pela facilidade de reprodução em Colab e pela restrição acadêmica de custo zero. Os scripts em `src/` demonstram a evolução para uma estrutura mais modular, adequada a ambientes produtivos.

## Evolução futura

Em uma evolução produtiva, estes módulos poderiam ser orquestrados por Cloud Composer, Cloud Run, Dataflow ou GitHub Actions.
