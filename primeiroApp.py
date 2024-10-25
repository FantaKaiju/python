import streamlit as st

# Título da página - url
st.title("Primeiro app :sunglasses:")
st.image("https://www.pontotel.com.br/local/wp-content/uploads/2022/05/imagem-corporativa.webp", width=800, )

st.header("Header com divisor", divider='rainbow')
st.subheader("Este é um subheader: _Streamlit é :blue[legal]")
st.write('Este é um *texto* normar')

'Texto mágico!'
texto = "Texto na Variável"
texto

st.markdown('Markdown: *Streamlit* é **realmente** ***legal***')
st.markdown('''
    :red[Streamlit] :orange[pode] :orange[escrever]
    :blue-background[texto destacado]
''')

st.text_input('Nome:')
st.slider('Qual sua idade?', 0, 120, 25)

opcoes = st.multiselect('Seleciona as cores que preferir:',
                        ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
                        ['Amarelo', 'Azul']
                        )
"Cores escolhidas"
st.write(opcoes)