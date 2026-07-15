# Estratégia de Versionamento

## 1. Contexto

O projeto foi desenvolvido individualmente por Andre Correa Luis Vilas Boas.

O controle de versão foi realizado com Git e GitHub, utilizando commits incrementais para registrar a evolução da pipeline.

Por não haver outros integrantes, não existiu um fluxo contínuo de colaboração, revisão entre pares ou divisão de funcionalidades entre membros da equipe.

## 2. Versionamento efetivamente utilizado

Durante o desenvolvimento foram utilizados:

- repositório Git;
- hospedagem no GitHub;
- branch principal `main`;
- commits incrementais;
- mensagens de commit relacionadas às etapas implementadas;
- histórico de evolução da solução.

Os commits registram atividades como:

- criação da estrutura do projeto;
- ingestão Batch;
- transformação Bronze, Silver e Gold;
- Streaming simulado;
- qualidade de dados;
- monitoramento;
- FinOps;
- documentação;
- correções finais.

## 3. Branches e Pull Requests

Durante a maior parte do projeto, o desenvolvimento ocorreu diretamente na branch `main`.

Essa decisão esteve relacionada ao caráter individual do trabalho e à ausência de outros colaboradores.

Mesmo em projetos individuais, branches e Pull Requests podem ser utilizadas para:

- isolar alterações;
- revisar diferenças antes do merge;
- registrar decisões;
- reduzir riscos sobre a branch principal;
- documentar uma etapa de correção.

Na revisão final foi criada a branch:

```text
fix/final-hardening
```

Essa branch concentra correções reais identificadas durante a auditoria final, incluindo:

- revisão da documentação;
- correção de inconsistências;
- limpeza de arquivos;
- atualização do README;
- fortalecimento da reprodutibilidade;
- adequação da entrega ao projeto efetivamente implementado.

Após as validações, a branch deverá ser integrada à `main` por meio de uma Pull Request de auto-revisão.

## 4. Pull Request de revisão final

A Pull Request final deverá registrar:

- objetivo da revisão;
- problemas encontrados;
- arquivos modificados;
- correções realizadas;
- verificações executadas;
- limitações conhecidas;
- resultado final.

A Pull Request não representa uma revisão por outro integrante. Ela funciona como evidência de controle de mudança e autoauditoria em um projeto individual.

## 5. Padrão de commits

O projeto utiliza mensagens curtas e descritivas, com prefixos como:

```text
feat:
fix:
docs:
```

Exemplos:

```text
feat: implementa transformação da camada gold
fix: corrige validações de qualidade
docs: atualiza documentação final
```

Esse padrão facilita a leitura do histórico e a identificação do tipo de alteração realizada.

## 6. Situação do versionamento

| Item | Situação |
|---|---|
| Repositório Git | Implementado |
| Repositório GitHub | Implementado |
| Histórico de commits | Implementado |
| Commits incrementais | Implementado |
| Desenvolvimento individual | Sim |
| Uso predominante da branch `main` | Sim |
| Branch de revisão final | Criada |
| Pull Request de revisão final | Pendente até a conclusão das correções |
| Revisão por outro integrante | Não se aplica |

## 7. Limitações

O projeto não utilizou, durante todo o ciclo de desenvolvimento:

- branches separadas para cada funcionalidade;
- revisão por pares;
- múltiplos colaboradores;
- Pull Requests em todas as etapas;
- integração contínua;
- proteção automática da branch `main`.

Esses itens podem ser adotados em uma evolução futura ou em um contexto de equipe.

## 8. Conclusão

O projeto possui versionamento real e verificável por meio do histórico de commits no GitHub.

A estratégia adotada refletiu o desenvolvimento individual. A branch e a Pull Request de revisão final complementam esse histórico, criando uma etapa explícita de validação antes da integração definitiva à branch principa