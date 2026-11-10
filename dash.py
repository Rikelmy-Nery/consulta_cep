import streamlit as st
import requests

st.set_page_config(
    layout='wide',
    page_title='Consulta CEP',
    page_icon='📍'
)

st.title('Consulta a CEP!')
st.divider()


def ConsultaCEP(cep):

    retorno = None
    try:
        dados = requests.get(url=f'https://viacep.com.br/ws/{cep}/json/')
        retorno = dados.json()
    except:
        retorno = 'Cep invalido tente novamente!'
    return retorno

cep = st.number_input(
    'Digite o seu CEP!',
    value=None,
    placeholder='29157061',
    max_value=99999999,
    help='Insira um CEP valido!'
    )
botao = st.button('Consultar')

if botao:
    renpose = ConsultaCEP(cep)
    try:
        if renpose['cep']:
            st.json(renpose)
    except:
        st.error(renpose)


