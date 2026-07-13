# Estratégia de Versionamento e Pull Requests

## 1. Objetivo

Este documento descreve a estratégia de versionamento utilizada no projeto **TechChallenge Fase 2 — Pipeline Híbrido para Análise da Alfabetização no Brasil**.

O objetivo é demonstrar organização do desenvolvimento, rastreabilidade das alterações e uso de boas práticas com Git e GitHub.

## 2. Repositório

Repositório do projeto:

```text
https://github.com/acorrea79/techchallenge-fase2-pipeline-alfabetizacao
```

## 3. Estratégia de branches

A branch principal do projeto é:

```text
main
```

Durante o desenvolvimento, as alterações foram organizadas por etapas funcionais da pipeline.

Para evidenciar boas práticas de versionamento, recomenda-se manter branches de consolidação, como:

```text
feature/code-organization
feature/final-documentation
feature/final-review
```

## 4. Padrão de commits

Os commits seguem uma estrutura simples baseada no tipo de alteração:

| Prefixo | Uso |
|---|---|
| `chore:` | Organização inicial, estrutura de pastas, ajustes de configuração |
| `docs:` | Documentação, README, diagramas e evidências |
| `feat:` | Novas funcionalidades da pipeline |
| `fix:` | Correções de código, validações ou ajustes de execução |
| `refactor:` | Reorganização de código sem alterar comportamento |
| `test:` | Testes e validações |

Exemplos de commits utilizados ou recomendados:

```text
chore: create initial project structure
docs: add initial README documentation
feat: add batch ingestion layer
feat: add silver transformation layer
feat: add gold analytical layer
feat: add simulated streaming pipeline
feat: add consolidated data quality checks
docs: add cloud bigquery and finops documentation
feat: add consolidated monitoring
feat: add modular source code structure
docs: update final readme and architecture documentation
docs: add final architecture diagrams
```

## 5. Pull Requests recomendados

Mesmo que parte do desenvolvimento tenha sido feita de forma incremental, recomenda-se registrar Pull Requests finais de consolidação para evidenciar o fluxo de revisão.

### PR 1 — Organização do código

Branch sugerida:

```text
feature/code-organization
```

Título sugerido:

```text
feat: add modular source code structure
```

Escopo:

- criação da pasta `src/`;
- organização dos scripts por responsabilidade;
- documentação da organização do código.

Arquivos principais:

```text
src/
docs/code_organization.md
```

### PR 2 — Documentação final

Branch sugerida:

```text
feature/final-documentation
```

Título sugerido:

```text
docs: finalize project documentation
```

Escopo:

- atualização final do README;
- documentação da arquitetura;
- diagramas finais;
- documentação de FinOps;
- documentação de monitoramento;
- evidências de uso do BigQuery Sandbox.

Arquivos principais:

```text
README.md
docs/
sql/
```

### PR 3 — Revisão final

Branch sugerida:

```text
feature/final-review
```

Título sugerido:

```text
docs: add final delivery review
```

Escopo:

- checklist de entrega;
- ajustes finais de documentação;
- organização dos artefatos finais.

## 6. Critérios de revisão dos PRs

Cada Pull Request deve observar:

- se os arquivos esperados foram criados;
- se a documentação está coerente com a execução do notebook;
- se os dados gerados não foram versionados indevidamente;
- se o README explica claramente a arquitetura;
- se Batch e Streaming estão descritos;
- se Qualidade, Monitoramento e FinOps estão documentados;
- se a estrutura do projeto está fácil de navegar.

## 7. Observação sobre dados gerados

Os arquivos gerados nas pastas abaixo são reproduzíveis e não devem ser versionados integralmente:

```text
data/bronze/
data/silver/
data/gold/
data/quality/
data/monitoring/
data/evidence/
logs/
```

A existência dessas pastas e seus fluxos é demonstrada pelo notebook, pelos manifestos e pela documentação.

## 8. Conclusão

A estratégia de versionamento adotada busca demonstrar evolução incremental, organização técnica e rastreabilidade da entrega.

O uso de commits semânticos, branches e Pull Requests facilita a avaliação do projeto e aproxima a entrega de uma prática profissional de engenharia de dados.
