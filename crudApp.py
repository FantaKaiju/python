import streamlit as st
import pandas as pd

# aba da aplicação
st.set_page_config(
    page_title= "Controle de Estoque",
    page_icon= ":shopping_trolley:"
)

def cadastra_produto():
    produto_id = st.text_input('ID')
    produto_nome = st.text_input('Nome')
    produto_preco = st.number_input('Preço', min_value=0.00)
    produto_estoque = st.number_input('Estoque', min_value=0)

    if st.button('Cadastrar Produto'):
        # Cria um novo DataFrame para o novo produto
        novo_produto = pd.DataFrame({
            'ID': [produto_id],
            'Nome': [produto_nome],
            'Preco': [produto_preco],
            'Estoque': [produto_estoque]
        })

        st.session_state['produtos'] = pd.concat([st.session_state['produtos'], novo_produto], ignore_index=True)
        st.success('Produto cadastrado com sucesso!')


# Função para mostrar todos os produtos
def listar_produtos():
    st.subheader('Todos os Produtos do Sistema')
    st.dataframe(st.session_state['produtos'])

# Função para deletar um produto
def apagar_produtos():
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox('Selecione a ID do produto para apagar', lista_produtos)

    if produto_id and st.button('Apagar Produto'):
        # Remove o produto pelo ID
        st.session_state['produtos'] = st.session_state['produtos'][st.session_state['produtos']['ID'] != produto_id]
        st.success('Produto apagado com sucesso!')

# Função para alterar um produto existente
def alterar_produto():
    # Converte a coluna ID em uma lista
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox('Selecione a ID do Produto para Alterar', lista_produtos)

    if produto_id:
        # Localiza o produto pelo ID
        produto = st.session_state['produtos'][st.session_state['produtos']['ID'] == produto_id].iloc[0]

        # Entrada de dados para atualizar produto
        novo_nome = st.text_input('Nome', value=produto['Nome'])
        novo_preco = st.number_input('Preço', min_value=0.00, value=produto['Preco'])
        novo_estoque = st.number_input('Estoque', min_value=0, value=int(produto['Estoque']))

        if st.button('Atualizar Produto'):
            st.session_state['produtos'].loc[
                st.session_state['produtos']['ID'] == produto_id, ['Nome', 'Preco', 'Estoque']] = \
                                                [novo_nome, novo_preco, novo_estoque]

            st.success('Produto atualizado com sucesso!')

if __name__ == "__main__":
    st.title('Controle de Estoque')

    # inicializa o DataFrame e salva na sessão
    if 'produtos' not in st.session_state:
        st.session_state['produtos'] = pd.DataFrame(columns=['ID', 'Nome', 'Preco', 'Estoque'])

# Controle da ação através de barra lateral
    opcao = st.sidebar.selectbox('Escolha uma opção', ['Cadastrar Produto', 'Alterar Produto', 'Apagar Produto', 'Listar Todos so produtos'])

    if opcao == 'Cadastrar Produto':
        cadastra_produto()
    elif opcao == 'Alterar Produto':
        alterar_produto()
    elif opcao == 'Apagar Produto':
        apagar_produtos()
    elif opcao == 'Listar Todos so produtos':
        listar_produtos()
