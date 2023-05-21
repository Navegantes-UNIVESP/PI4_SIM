import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Integrantes",
    page_icon=":construction_worker:",
)

image = Image.open('logo_univesp.png')
st.image(image)

st.write('#### [Universidade Virtual do Estado de São Paulo (UNIVESP)](https://univesp.br)')
st.write('#### [:octocat: Github do Projeto](https://github.com/Navegantes-UNIVESP/PI4_SIM)')


st.write("# Integrantes 👋")

st.markdown(
    """
    ### Ciência de Dados
    - Gabriel Nascimento Silva, 2006400
    - Geovanni Evangelista dos Santos, 2003025
    - Marcos Pereira da Silva Cruz, 2000561

    ### Engenharia da Computação
    - Alexandre Marques Agostinho, 2011582
    - Fabio Martins dos Santos, 2009467
    - Felipe Rafael da Silva Oliveira, 2012776
    - Maria Elizangela Linhares, 2006684

    ### Orientador
    - Daniel Spinoso Prado
"""
)


