import pandas as pd
import sqlite3 # Importando o motor de banco de dados nativo do Python

# 1. EXTRAÇÃO (Extract)
print("Iniciando a extração dos dados da Steam...")
df_jogos = pd.read_csv('steam_games_raw.csv')

print("\n--- Dados Brutos (Raw Data) ---")
print(df_jogos)

# 2. TRANSFORMAÇÃO (Transform)
print("\nIniciando a limpeza e transformação dos dados...")

# Passo A: O "Filtro de Qualidade"
df_limpo = df_jogos.dropna().copy()

# Passo B: Criando inteligência
df_limpo['ApprovalRating(%)'] = (df_limpo['PositiveReviews'] / df_limpo['TotalReviews']) * 100

# Passo C: Estética
df_limpo['ApprovalRating(%)'] = df_limpo['ApprovalRating(%)'].round(2)

print("\n--- Dados Transformados (Clean Data) ---")
print(df_limpo)

# 3. CARREGAMENTO (Load)
print("\nIniciando o carregamento no Banco de Dados...")

# Cria um arquivo de banco de dados chamado "steam_catalog.db" (ou conecta se já existir)
conexao = sqlite3.connect('steam_catalog.db')

# Salva a nossa tabela limpa dentro do banco de dados, com o nome "tb_jogos_aprovados"
# if_exists='replace' garante que se rodarmos o script de novo, ele atualiza a tabela
df_limpo.to_sql('tb_jogos_aprovados', conexao, if_exists='replace', index=False)

# Fecha a conexão com o banco (boa prática de segurança e performance)
conexao.close()

print("\nETL Finalizado com sucesso! Dados salvos em 'steam_catalog.db'.")