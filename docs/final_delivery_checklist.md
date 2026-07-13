# Checklist de Revisão Final da Entrega

## 1. Estrutura do projeto

- [ ] `README.md` presente na raiz.
- [ ] `requirements.txt` presente na raiz.
- [ ] `.gitignore` configurado.
- [ ] `notebooks/pipeline_alfabetizacao_colab.ipynb` presente.
- [ ] Pasta `src/` criada e organizada.
- [ ] Pasta `docs/` com documentação final.
- [ ] Pasta `sql/` com consultas auxiliares.

## 2. Pipeline Batch

- [ ] Ingestão Batch documentada.
- [ ] Bronze Batch gerada em CSV.
- [ ] Silver gerada em Parquet.
- [ ] Gold gerada em Parquet.
- [ ] Tabela `alunos` tratada com estratégia de amostra e agregação.

## 3. Streaming

- [ ] Producer simulado criado.
- [ ] Eventos JSONL gerados.
- [ ] Micro-batches processados.
- [ ] Eventos inválidos enviados para quarentena.
- [ ] Gold Streaming gerada.
- [ ] Monitoramento do streaming documentado.

## 4. Qualidade

- [ ] Validação de arquivos.
- [ ] Validação de colunas obrigatórias.
- [ ] Validação de nulos.
- [ ] Validação de duplicidades.
- [ ] Validação de faixas percentuais.
- [ ] Validação de chaves.
- [ ] Status final sem falhas críticas.

Resultado esperado:

```text
executive_quality_status: approved_with_warnings
failed_checks: 0
```

## 5. Monitoramento

- [ ] Monitoramento consolidado gerado.
- [ ] Alertas documentados.
- [ ] Status executivo sem falhas críticas.

Resultado esperado:

```text
executive_monitoring_status: approved_with_warnings
failed_components: 0
critical_alerts: 0
```

## 6. Cloud / BigQuery / FinOps

- [ ] BigQuery Sandbox utilizado.
- [ ] Evidências documentadas.
- [ ] Estratégia FinOps documentada.
- [ ] Uso de Parquet justificado.
- [ ] Uso de amostra e agregação justificado.
- [ ] Restrição de custo zero documentada.

## 7. Documentação

- [ ] README final completo.
- [ ] Arquitetura documentada.
- [ ] Diagramas finais adicionados.
- [ ] Organização do código documentada.
- [ ] Estratégia de monitoramento documentada.
- [ ] Estratégia FinOps documentada.
- [ ] Estratégia de versionamento documentada.

## 8. GitHub

- [ ] Commits com mensagens claras.
- [ ] Branches ou PRs de consolidação criados.
- [ ] Nenhum dado grande versionado indevidamente.
- [ ] Nenhuma credencial enviada ao repositório.

## 9. Vídeo

- [ ] Roteiro preparado.
- [ ] Problema de negócio explicado.
- [ ] Arquitetura explicada.
- [ ] Batch explicado.
- [ ] Streaming explicado.
- [ ] Qualidade, monitoramento e FinOps explicados.
- [ ] Potencial de IA explicado.
