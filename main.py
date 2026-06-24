import pandas as pd
import sqlite3
#extract
print("Iniciando a extração dos dados da Steam...")
df_jogos = pd.read_csv('steam_games_raw.csv')

print("\n--- Dados Brutos (Raw Data) ---")
print(df_jogos)

#transform
print("\nIniciando a limpeza e transformação dos dados...")

df_limpo = df_jogos.dropna().copy()

df_limpo['ApprovalRating(%)'] = (df_limpo['PositiveReviews'] / df_limpo['TotalReviews']) * 100

df_limpo['ApprovalRating(%)'] = df_limpo['ApprovalRating(%)'].round(2)

print("\n--- Dados Transformados (Clean Data) ---")
print(df_limpo)

#load
print("\nIniciando o carregamento no Banco de Dados...")

#cria um arquivo de banco de dados
conexao = sqlite3.connect('steam_catalog.db')

df_limpo.to_sql('tb_jogos_aprovados', conexao, if_exists='replace', index=False)

conexao.close()

print("\nDados salvos em 'steam_catalog.db'.")