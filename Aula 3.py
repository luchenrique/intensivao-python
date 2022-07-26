"""
# Automação Web e Busca de Informações com Python

#### Desafio: 

Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
- Dólar
- Euro
- Ouro

Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.

Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing

Para isso, vamos criar uma automação web:

- Usaremos o selenium
- Importante: baixar o webdriver
"""

!pip install selenium
# Chromedriver

from selenium import webdrive
from selenium.webdrive.common.keys import Keys

# Passo 1: Pegar a cotação do dólar
#abrir o navegador
navegador = webdrive.Chrome()

# Entrar no google
navegador.get("https://www.google.com.br/")

# Pesquisar cotação dolar no google
navegador.find_element('xpath', '//html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element('xpath', '//html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Pegar a cotação
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(cotacao_dolar)
# Passo 2: Pegar a cotação do euro
# Entrar no google
navegador.get("https://www.google.com.br/")

# Pesquisar cotação dolar no google
navegador.find_element('xpath', '//html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath', '//html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Pegar a cotação
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

# Passo 3: Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/")

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
print(cotacao_ouro)

# Passo 6: Exportar a base de dados

"""### Agora vamos atualiza a nossa base de preços com as novas cotações

- Importando a base de dados
"""

# Passo 4: Atualizar a base de dados
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

"""- Atualizando os preços e o cálculo do Preço Final"""

# Passo 5: Recalcular os preços

# Atualizar as cotações
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)]
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)]
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)]

# Preço de compra = Preço original * Cotação
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# Preco de venda = Preco de compra * margem 
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
display(tabela)

"""### Agora vamos exportar a nova base de preços atualizada"""

# Passo 6: Exportar a base de dados
tabela.to_excel("Produtos Novo.xlsx", index=False)
