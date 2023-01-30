import pandas as pd

# Carregando os dados para o dataframe
df = pd.read_csv('dados.csv')

# Convertendo a coluna "Time" para o tipo datetime
df['Time'] = pd.to_datetime(df['Time'])

# Verificando se há valores faltantes na coluna "Outdoor Humidity(%)"
print(df['Outdoor Humidity(%)'].isnull().sum())

# Substituindo os valores faltantes na coluna "Outdoor Humidity(%)" com a média dos valores existentes
df['Outdoor Humidity(%)'] = df['Outdoor Humidity(%)'].fillna(df['Outdoor Humidity(%)'].mean())

# Verificando se há valores faltantes na coluna "Outdoor Humidity(%)" após a substituição
print(df['Outdoor Humidity(%)'].isnull().sum())

# Removendo a coluna "NO." já que não é relevante para a análise
df = df.drop('NO.', axis=1)

# Salvando o dataframe limpo em um novo arquivo csv
df.to_csv('dados_limpos.csv', index=False)
