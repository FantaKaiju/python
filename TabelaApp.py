import streamlit as st
import pandas as pd
import openpyxl

# Cria um dicionário para simular dados
dados=  {
    'Nome do produto' : ['Semáforo', 'Cafeteira', 'Reboco', 'Gengibre'],
    'Descrição' : ['Semáforo de Fórmula 1', 'Cafeteira Brastemp', 'Reboco de rebocar', 'Gengibre de gengibre'],
    'Preço' : [5.99, 158.99, 2.99, 30000.00],
    'Quantidade em Estoque' : [40, 7, 222, 15]
}

# Converte dicionário em DataFrame
df1 = pd.DataFrame(dados)

# Exibe o DataFrame
st.subheader('DataFrame a partir do dicionário de dados')
st.dataframe(df1)

# Define URL do arquivo do Excel
url = 'https://softgraf.com/cursodatascience/produtos.xlsx'

# Lê o arquivo da url e converte em DataFrame
df2 = pd.read_excel(url, engine = openpyxl)

# Exibe o DataFrame
st.subheader('DataFrame a partir do arquivo do Excel')
st.dataframe(df2)
