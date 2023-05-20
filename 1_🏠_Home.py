import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write(" # Bem vindo à Plataforma da Longevidade! 👋")

st.sidebar.success("Selecione uma página acima")

st.markdown(
    """
    ### As características que influenciam o tempo de vida

    A busca pela longevidade sempre foi uma das maiores aspirações da humanidade. Porém, muitos fatores podem afetar a saúde e reduzi-la, como as doenças e eventos que ocorrem ao longo da vida de uma pessoa.
    
    ### Análise de dados reais para uma compreensão aprofundada

    Com o objetivo de prever a longevidade em relação a esses fatores, usamos o **[Sistema de Informações sobre Mortalidade (SIM) do DATASUS](https://opendatasus.saude.gov.br/dataset/sim-1979-2022)**, referentes ao período de **2021**. Através desses dados, é possível observar que algumas doenças que têm um impacto significativo na mortalidade da população brasileira.

    ### Predição com *Machine Learning*

    Esta plataforma apresenta um modelo de *Machine Learning* denominado [XGBoost](https://xgboost.readthedocs.io/en/stable/). Aqui buscamos oferecer uma compreensão mais ampla da relação entre a longevidade humana e os eventos relacionados a vida do usuário.
    
    :no_entry: *As predições apresentadas refletem um trabalho inicial e não devem ser usadas em decisões médicas ou pessoais.*

"""
)