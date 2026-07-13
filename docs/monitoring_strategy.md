
# Estratégia de Monitoramento

## 1. Objetivo

Este documento descreve a estratégia de monitoramento adotada na pipeline híbrida para análise da alfabetização no Brasil.

O monitoramento consolida informações das camadas Batch, Streaming, Qualidade, FinOps e Logs.

## 2. Componentes monitorados

A solução monitora:

- Bronze Batch;
- Silver Transform;
- Gold Analytics;
- Streaming Simulado;
- Data Quality;
- Cloud / BigQuery / FinOps;
- arquivos obrigatórios do repositório;
- logs de execução.

## 3. Métricas acompanhadas

As principais métricas acompanhadas são:

- quantidade de datasets processados;
- total de linhas processadas;
- arquivos gerados;
- status por camada;
- duplicidades removidas;
- eventos de streaming recebidos;
- eventos válidos e inválidos;
- taxa de eventos inválidos;
- latência média e máxima do streaming;
- quantidade de checks de qualidade;
- checks aprovados, warnings e falhas;
- bytes estimados em consultas BigQuery;
- alertas operacionais.

## 4. Streaming

O streaming simulado gera métricas específicas:

- total de eventos gerados;
- total de eventos válidos;
- total de eventos inválidos;
- taxa de inválidos;
- total de micro-batches;
- latência média;
- latência máxima;
- arquivo de quarentena.

Eventos inválidos são enviados para quarentena para demonstrar governança e tratamento de falhas.

## 5. Qualidade de Dados

O monitoramento utiliza o resultado da qualidade consolidada.

Status final da qualidade na última execução:

- Status: `approved_with_warnings`
- Checks aprovados: `126`
- Warnings: `6`
- Falhas críticas: `0`

## 6. Alertas

Os alertas são classificados em:

- `critical`: falhas críticas que impedem considerar a pipeline saudável;
- `warning`: alertas controlados ou esperados;
- `info`: eventos informativos.

Na execução monitorada:

- Alertas críticos: `0`
- Alertas warning: `7`
- Total de alertas: `7`

## 7. Status executivo

Status executivo do monitoramento:

`approved_with_warnings`

Interpretação:

Monitoramento aprovado com alertas controlados.

## 8. Evolução futura

Em ambiente produtivo, a estratégia poderia evoluir para:

- Cloud Monitoring;
- alertas automáticos por e-mail ou Slack;
- métricas customizadas no BigQuery;
- dashboards em Looker Studio;
- orquestração com Cloud Composer;
- monitoramento em tempo real de Pub/Sub e Dataflow.

## 9. Conclusão

O projeto possui observabilidade mínima por meio de logs, manifestos, relatórios de qualidade, relatórios de streaming, métricas de FinOps e resumo executivo consolidado.
