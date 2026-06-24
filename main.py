import pandas as pd

# 1. EXTRAÇÃO (Extract)
print("Iniciando a extração dos dados da Steam...")
df_jogos = pd.read_csv('steam_games_raw.csv')

print("\n--- Dados Brutos (Raw Data) ---")
print(df_jogos)

# 2. TRANSFORMAÇÃO (Transform)
print("\nIniciando a limpeza e transformação dos dados...")

# Passo A: O "Filtro de Qualidade"
# Remove sumariamente qualquer linha que contenha dados vazios (NaN)
df_limpo = df_jogos.dropna().copy()

# Passo B: Criando inteligência
# Vamos calcular a porcentagem real de avaliações positivas de cada jogo
df_limpo['ApprovalRating(%)'] = (df_limpo['PositiveReviews'] / df_limpo['TotalReviews']) * 100

# Passo C: Estética
# Arredonda o valor da nova coluna para apenas 2 casas decimais
df_limpo['ApprovalRating(%)'] = df_limpo['ApprovalRating(%)'].round(2)

print("\n--- Dados Transformados (Clean Data) ---")
print(df_limpo)