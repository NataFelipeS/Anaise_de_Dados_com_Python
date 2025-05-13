import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração para exibir mais colunas
pd.set_option('display.max_columns', None)

# 1. Series - estrutua unidimensional semelhante a um array ou lista
print("1. Trabalhando com Series")
print("-" * 50)



# Criando uma Series com índices personalizados
s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Series com índices personalizados:")
print(s2)
print()

# Criando uma Series a partir de um dicionário
dicionario = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
s3 = pd.Series(dicionario)
print("Series criada a partir de um dicionário:")
print(s3)
print()

# Acessando elementos de uma Series
print("Acessando elementos da Series:")
print("Elemento no índice 'a':", s3['a'])
print("Elementos nos índices 'a', 'c' e 'e':", s3[['a', 'c', 'e']])
print()

# Operações com Series
print("Operações com Series:")
print("s2 + 5:")
print(s2 + 5)
print("\ns2 * 2:")
print(s2 * 2)
print()

# 2. DataFrames - estrutura bidimensional semelhante a uma tabela
print("2. Trabalhando com DataFrames")
print("-" * 50)

# Criando um DataFrame a partir de um dicionário
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [25, 30, 35, 40, 45],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador'],
    'Salário': [5000, 6000, 7000, 8000, 9000]
}

df1 = pd.DataFrame(dados)
print("DataFrame criado a partir de um dicionário:")
print(df1)
print()

# Informações sobre o DataFrame
print("Informações sobre o DataFrame:")
print("Shape (linhas, colunas):", df1.shape)
print("\nTipos de dados:")
print(df1.dtypes)
print("\nPrimeiras 3 linhas:")
print(df1.head(3))
print("\nÚltimas 2 linhas:")
print(df1.tail(2))
print("\nResumo estatístico das colunas numéricas:")
print(df1.describe())
print()

# Acessando dados do DataFrame
print("Acessando dados do DataFrame:")
print("Coluna 'Nome':")
print(df1['Nome'])
print("\nColunas 'Nome' e 'Idade':")
print(df1[['Nome', 'Idade']])
print("\nPrimeira linha:")
print(df1.iloc[0])
print("\nLinhas 1 a 3:")
print(df1.iloc[1:4])
print("\nValor na linha 2, coluna 'Salário':")
print(df1.iloc[2, 3])  # ou df1.loc[2, 'Salário']
print()

# Filtragem de dados
print("Filtragem de dados:")
print("Pessoas com idade maior que 30:")
print(df1[df1['Idade'] > 30])
print("\nPessoas de São Paulo ou Salvador:")
print(df1[df1['Cidade'].isin(['São Paulo', 'Salvador'])])
print()

# Criando novas colunas
print("Criando novas colunas:")
df1['Faixa Etária'] = ['Jovem' if idade < 30 else 'Adulto' if idade < 40 else 'Sênior' for idade in df1['Idade']]
df1['Bônus'] = df1['Salário'] * 0.1
print(df1)
print()

# Agrupamento de dados
print("Agrupamento de dados:")
print("Média de salário por faixa etária:")
print(df1.groupby('Faixa Etária')['Salário'].mean())
print("\nContagem por faixa etária:")
print(df1.groupby('Faixa Etária').size())
print()

import datetime
# 3. Leitura e escrita de dados
print("3. Leitura e escrita de dados")
print("-" * 50)

def generate_random_date():
    year = np.random.randint(2020, 2025)
    month = np.random.randint(1, 13)
    day = np.random.randint(1, 28)
    return datetime.datetime(year, month, day)

# Criando um DataFrame para salvar
df_exemplo = pd.DataFrame({
    'A': np.random.rand(5),
    'B': np.random.randint(0, 10, 5),
    'C': ['a', 'b', 'c', 'd', 'e'],
    'date': [generate_random_date() for _ in range(5)]
})

print("DataFrame para demonstração de I/O:")
print(df_exemplo)
print()

df_exemplo.to_csv('exemplo.csv', index=False)

with open('exemplo.csv', 'r') as f:
    csv = f.read()

print(csv)

df_csv = pd.read_csv('exemplo.csv')
df_csv

# Salvando em diferentes formatos (comentado para não criar arquivos)
print("Exemplos de como salvar DataFrames (código comentado):")
print("# Salvar como CSV")
print("# df_exemplo.to_csv('exemplo.csv', index=False)")
print("\n# Salvar como Excel")
print("# df_exemplo.to_excel('exemplo.xlsx', index=False)")
print("\n# Salvar como JSON")
print("# df_exemplo.to_json('exemplo.json')")
print()

print("Exemplos de como ler arquivos (código comentado):")
print("# Ler CSV")
print("# df_csv = pd.read_csv('exemplo.csv')")
print("\n# Ler Excel")
print("# df_excel = pd.read_excel('exemplo.xlsx')")
print("\n# Ler JSON")
print("# df_json = pd.read_json('exemplo.json')")
print()

# 4. Visualização básica de dados
print("4. Visualização básica de dados")
print("-" * 50)

# Criando dados para visualização
df_vis = pd.DataFrame({
    'x': range(1, 11),
    'y1': np.random.rand(10) * 10,
    'y2': np.random.rand(10) * 10 + 5
})

print("DataFrame para visualização:")
print(df_vis)
print()

df_vis

print("Para visualizar os gráficos, execute as células abaixo:")
print("# Gráfico de linha")
print("plt.figure(figsize=(10, 6))")
print("plt.plot(df_vis['x'], df_vis['y1'], 'b-', label='Série 1')")
print("plt.plot(df_vis['x'], df_vis['y2'], 'r--', label='Série 2')")
print("plt.title('Gráfico de Linha Simples')")
print("plt.xlabel('Eixo X')")
print("plt.ylabel('Eixo Y')")
print("plt.legend()")
print("plt.grid(True)")
print("plt.show()")
print()

print("# Gráfico de barras")
print("plt.figure(figsize=(10, 6))")
print("df1.plot(kind='bar', x='Nome', y='Salário')")
print("plt.title('Salários por Pessoa')")
print("plt.xlabel('Nome')")
print("plt.ylabel('Salário (R$)')")
print("plt.xticks(rotation=45)")
print("plt.tight_layout()")
print("plt.show()")

# Gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(df_vis['x'], df_vis['y1'], 'b-', label='Série 1')
plt.plot(df_vis['x'], df_vis['y2'], 'r--', label='Série 2')
plt.title('Gráfico de Linha Simples')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de barras
plt.figure(figsize=(10, 6))
df1.plot(kind='bar', x='Nome', y='Salário')
plt.title('Salários por Pessoa')
plt.xlabel('Nome')
plt.ylabel('Salário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(df_vis['x'], df_vis['y1'], 'b-', label='Série 1')
plt.plot(df_vis['x'], df_vis['y2'], 'r--', label='Série 2')
plt.title('Gráfico de Linha Simples')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
df1.plot(kind='bar', x='Nome', y='Salário')
plt.title('Salários por Pessoa')
plt.xlabel('Nome')
plt.ylabel('Salário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()