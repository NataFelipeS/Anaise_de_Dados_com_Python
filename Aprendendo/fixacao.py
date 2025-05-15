import pandas as pd

dados = pd.read_csv(r"C:\\Users\\T-Gamer\\Documents\\GitHub\\An-lise-de-Dados-com-Python\\Aprendendo\\test_data_grande.csv")

print(dados)
print('-' * 80)

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79']
dados['faixa_idade'] = pd.cut(dados['idade'], bins=bins, labels=labels, right=False)

print(dados)

print('-' * 80)

resumo = (
dados
.groupby('faixa_idade')
.agg(
    media_salario=('salario','mean'),
    count_empregaods=('id', 'count')
)
.reset_index()
)

print(resumo)

print(dados['idade'].max())

# corte = dados[['id', 'nome', 'idade']]
# print(corte)
