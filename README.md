# ETL Pipeline: Catálogo da Steam

Projeto prático de Extração, Transformação e Carregamento (ETL) focado em higienização de dados e geração de métricas de negócio.

## Objetivo do Projeto
Construir um pipeline de dados automatizado capaz de consumir uma base bruta de jogos da loja Steam, aplicar regras de tratamento para limpeza de valores inconsistentes e exportar o resultado estruturado para um Banco de Dados Relacional. 

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python 3:** Lógica principal e orquestração do script.
* **Pandas:** Manipulação de DataFrames, limpeza de valores nulos (`NaN`) e criação de colunas calculadas.
* **SQLite3:** Motor de banco de dados relacional leve para a etapa de carregamento (Load).
* **Git/GitHub:** Versionamento de código e documentação.

## Arquitetura do Pipeline

1. **Extract (Extração):**
   * Leitura de um arquivo `.csv` contendo dados brutos e desestruturados.
   * Carregamento das informações em memória através de DataFrames do Pandas.

2. **Transform (Transformação):**
   * **Limpeza de Qualidade:** Remoção sumária de registros com dados vitais em branco.
   * **Geração de Inteligência:** Cálculo automático da taxa de aprovação real (`ApprovalRating(%)`) baseada no cruzamento entre "Reviews Positivos" e "Total de Reviews".
   * **Padronização:** Arredondamento de métricas numéricas para duas casas decimais.

3. **Load (Carregamento):**
   * Conexão nativa com banco de dados `.db` via motor SQLite.
   * Conversão automática do DataFrame em comandos SQL para popular a tabela `tb_jogos_aprovados`.
