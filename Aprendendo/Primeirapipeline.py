import pandas as pd
from sqlalchemy import create_engine
import json

dados = pd.read_csv(r"C:\\Users\\T-Gamer\Documents\\GitHub\\An-lise-de-Dados-com-Python\\Aprendendo\\test_data.csv")

dados_limpos = dados.fillna(0)

print(dados_limpos)

dados['idade_meses'] = dados['idade'] * 12
print(dados)

print('-' * 80)

dados['data_contratacao'] = pd.to_datetime(dados['data_contratacao'], format='%Y-%m-%d')
hoje = pd.Timestamp.today()
dados['anos_de_casa'] = (hoje - dados['data_contratacao']).dt.days / 365
print(dados)

print('-' * 80)

consulta = dados[dados['anos_de_casa'] > 5]
print(consulta)

print('-' * 80)

bins = [0, 25, 30, 40, 50]
labels = ['0-25','26-29', '30-39', '40-49']
dados['faixa_idade'] = pd.cut(dados['idade'], bins=bins, labels=labels)

resumo = (
    dados
    .groupby('faixa_idade')
    .agg(
        media_salario=('salario', 'mean'),
        count_empregados=('id', 'count')
    )
    .reset_index()
)

print(resumo)

# df_small = dados[['id', 'nome', 'salario']]

# print(df_small)

