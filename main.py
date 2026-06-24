import pandas as pd

# 1. EXTRAÇÃO (Extract)
print("Iniciando a extração dos dados da Steam...")

# Lendo o arquivo CSV e transformando em um DataFrame (tabela inteligente do Pandas)
df_jogos = pd.read_csv('steam_games_raw.csv')

# Exibindo os dados brutos no terminal para conferência
print("\n--- Dados Brutos (Raw Data) ---")
print(df_jogos)