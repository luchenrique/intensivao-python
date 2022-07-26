"""
# Análise de Dados com Python

### Desafio:

Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset
"""

# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")


# Passo 2: Visualizar a base de dados
# Entender a informações que você tem disponível 
# Descobrir os erros da base de dados

# Excluir coluna irrelevante
# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna
tabela =  tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# Passo 3: Tratamento de dados 
# Informações do tipo correto - ajustar o TotalGasto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Informações vazias
# Colunas completamente vazias
tabela = tabela.dropna(how="all", axis=1)

# Linhas que tem alguma informação vazia
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: Análise Inicial dos dados
# Como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise Mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento
import plotly.express as px

# etapa 1: criar o gráfico
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # etapa 2: exibir o gráfico
    grafico.show()
