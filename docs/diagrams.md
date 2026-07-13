# Diagramas Finais da Arquitetura

## 1. Visão Geral da Solução

```mermaid
flowchart TD
    A[Base dos Dados / BigQuery Sandbox] --> B[Google Colab / Python]

    B --> C[Bronze Batch]
    B --> D[Bronze Streaming]

    C --> E[Silver Batch]
    D --> F[Silver Streaming]

    E --> G[Gold Analytics]
    F --> H[Gold Streaming]

    G --> I[Qualidade Consolidada]
    H --> I

    I --> J[Monitoramento Consolidado]
    J --> K[Documentação / Evidências / FinOps]

    G --> L[Base Analítica para IA]
```

## 2. Pipeline Batch

```mermaid
flowchart LR
    A[BigQuery Público<br/>Base dos Dados] --> B[Consulta Batch<br/>Python + BigQuery Client]
    B --> C[Bronze CSV<br/>Dados brutos]
    C --> D[Silver Parquet<br/>Dados tratados]
    D --> E[Gold Parquet<br/>Bases analíticas]
    E --> F[Qualidade]
    F --> G[Monitoramento]
```

## 3. Pipeline Streaming Simulado

```mermaid
flowchart LR
    A[Producer Python] --> B[Eventos JSONL]
    B --> C[Bronze Streaming]
    C --> D[Consumer Micro-batch]
    D --> E{Validação do Evento}

    E -->|Evento válido| F[Silver Streaming]
    E -->|Evento inválido| G[Quarentena]

    F --> H[Gold Streaming]
    H --> I[Resumo de Eventos]
    I --> J[Monitoramento]
```

## 4. Arquitetura Medalhão

```mermaid
flowchart TD
    A[Bronze<br/>Dados brutos e eventos originais] --> B[Silver<br/>Dados limpos, padronizados e validados]
    B --> C[Gold<br/>Bases analíticas finais]

    C --> D[Indicador Município]
    C --> E[Indicador UF]
    C --> F[Comparativo Meta x Resultado]
    C --> G[Ranking Municípios Prioritários]
    C --> H[Base para IA]
```

## 5. Qualidade de Dados

```mermaid
flowchart TD
    A[Arquivos Bronze, Silver, Gold e Streaming] --> B[Validação de Existência]
    B --> C[Validação de Colunas Obrigatórias]
    C --> D[Validação de Nulos]
    D --> E[Validação de Duplicidade]
    E --> F[Validação de Faixas Percentuais]
    F --> G[Validação de Chaves e Consistência]
    G --> H[Relatório Consolidado de Qualidade]
    H --> I{Status Executivo}

    I -->|Sem falhas críticas| J[approved / approved_with_warnings]
    I -->|Com falhas críticas| K[failed]
```

## 6. Monitoramento Consolidado

```mermaid
flowchart TD
    A[Manifesto Batch] --> G[Monitoramento Consolidado]
    B[Manifesto Silver] --> G
    C[Manifesto Gold] --> G
    D[Monitoramento Streaming] --> G
    E[Relatório de Qualidade] --> G
    F[Evidências FinOps] --> G

    G --> H[Registros de Monitoramento]
    G --> I[Alertas]
    G --> J[Resumo Executivo]

    J --> K[approved_with_warnings<br/>sem falhas críticas]
```

## 7. FinOps e Custo Zero

```mermaid
flowchart LR
    A[Restrição: custo zero] --> B[BigQuery Sandbox]
    A --> C[Google Colab]
    A --> D[Sem billing ativo]

    B --> E[Dry Run para estimar bytes]
    B --> F[Consulta controlada da tabela alunos]

    F --> G[Amostra de alunos]
    F --> H[Agregação por município/rede/série]

    G --> I[Redução de custo]
    H --> I

    I --> J[Parquet em Silver/Gold]
```

## 8. Aplicação em IA

```mermaid
flowchart TD
    A[Gold Base IA Alfabetização] --> B[Features Educacionais]
    B --> C[Taxa de Alfabetização]
    B --> D[Meta de Referência]
    B --> E[Distância da Meta]
    B --> F[UF / Município / Rede / Série]

    C --> G[Modelo Preditivo Futuro]
    D --> G
    E --> G
    F --> G

    G --> H[Priorização de Municípios]
    G --> I[Análise de Risco]
    G --> J[Apoio à Política Pública]
```

## 9. Resumo Visual da Entrega

```mermaid
flowchart TD
    A[Dados Públicos Educacionais] --> B[Pipeline Híbrida]
    B --> C[Batch]
    B --> D[Streaming Simulado]

    C --> E[Medalhão]
    D --> E

    E --> F[Bronze]
    E --> G[Silver]
    E --> H[Gold]

    H --> I[Qualidade]
    I --> J[Monitoramento]
    J --> K[FinOps]
    K --> L[Base para IA]
    L --> M[Entrega Final Documentada]
```

## 10. Observação

Os diagramas foram escritos em Mermaid para renderização automática no GitHub.  
Eles complementam o README e o arquivo `docs/architecture.md`.
