import streamlit as st

# Valores default
nome = ''
preco = 0.00
quantidade = 10

# configurações da página
st.set_page_config (
    page_title="Cadastro de Produtos",
    page_icon=":shopping_trolley:",
    layout="wide"
)

st.title('Cadastrar')
st.subheader('Formulário para cadastrar produtos')

# Cria o formulário
with st.form(key="form_produto"):
    nome = st.text_input('Nome de Produto', max_chars=60, placeholder="Descrição do produto", value=nome)
    preco = st.number_input('Preço do Produto', min_value=0.00, step=0.01, value=preco)
    quantidade = st.number_input('Quantidade em Estoque', min_value=0, step=0, value=quantidade)

    # True or False
    Enviar = st.form_submit_button(label='Enviar')

    # Ação quando o formulário é enviado
    if Enviar:
        st.success('Produto cadastrado com sucesso!')
        st.write(f'**Nome:** {nome}')
        st.write(f'**Preço:** {preco}')
        st.write(f'**Quantidade Disponível:** {quantidade}')