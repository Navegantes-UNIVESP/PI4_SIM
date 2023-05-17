
import xgboost as xgb
import streamlit as st
import pandas as pd
from PIL import Image


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-abstract-background-design_361591-1242.jpg?w=2000");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('PI4_5CIDS_xgb_model.json')

#Caching the model for faster loading
@st.cache_data


# Define the prediction function
def predict(ESC, ESTCIV, RACACOR, SEXO, CAUSABAS_E149, CAUSABAS_I10, CAUSABAS_I219, CAUSABAS_I64,CAUSABAS_J189, cid):
    
    CAUSABAS_E149 = 0
    CAUSABAS_I10 = 0
    CAUSABAS_I219 = 0
    CAUSABAS_I64 = 0
    CAUSABAS_J189 = 0

    # SEXO - 0: Ignorado 1: Masculino 2: Feminino
    if SEXO == 'Não quero informar':
        SEXO = 0
    elif SEXO == 'Masculino':
        SEXO = 1
    elif SEXO == 'Feminino':
        SEXO = 2

    # RACACOR - 1: Branca 2: Preta 3: Amarela 4: Parda 5: Indígena
    if RACACOR == 'Branca':
        RACACOR = 1
    elif RACACOR == 'Preta':
        RACACOR = 2
    elif RACACOR == 'Amarela':
        RACACOR = 3
    elif RACACOR == 'Parda':
        RACACOR = 4
    elif RACACOR == 'Indígena':
        RACACOR = 5

    # ESTCIV, conforme a tabela: 1: Solteiro 2: Casado 3: Viúvo 
    # 4: Separado judicialmente 5: União consensual (versões anteriores)9: Ignorado
    if ESTCIV == 'Solteiro':
        ESTCIV = 1
    elif ESTCIV == 'Casado':
        ESTCIV = 2
    elif ESTCIV == 'Viúvo':
        ESTCIV = 3
    elif ESTCIV == 'Separado judicialmente':
        ESTCIV = 4
    elif ESTCIV == 'União consensual':
        ESTCIV = 5
    elif ESTCIV == 'Não quero informar':
        ESTCIV = 9
    
    # ESC Escolaridade, Anos de estudo concluídos: 1: 
    # Nenhuma 2: 1 a 3 anos 3: 4 a 7 anos 4: 8 a 11 anos 5: 12 e mais 9: Ignorado
    if ESC == 'Não estudei formalmente':
        ESC = 1
    elif ESC == '1 a 3 anos':
        ESC = 2
    elif ESC == '4 a 7 anos':
        ESC = 3
    elif ESC == '8 a 11 anos':
        ESC = 4
    elif ESC == '12 e mais':
        ESC = 5
    elif ESC == 'Não quero informar':
        ESC = 9

    # # CIDS 'I219', 'I10', 'I64', 'J189', 'E149'
    # # Nenhuma 2: 1 a 3 anos 3: 4 a 7 anos 4: 8 a 11 anos 5: 12 e mais 9: Ignorado
    if cid == 'CID I219 - Infarto agudo do miocárdio':
        CAUSABAS_I219 = 1
    elif cid == 'CID I10 - Hipertensão essencial (Primária)':
        CAUSABAS_I10 = 1
    elif cid == 'CID I64 - Acidente vascular cerebral':
        CAUSABAS_I64 = 1
    elif cid == 'CID J189 - Pneumonia por microorganismo':
        CAUSABAS_J189 = 1
    elif cid == 'CID E149 - Diabetes mellitus':
        CAUSABAS_E149 = 1
    

    prediction = model.predict(pd.DataFrame([[ESC, ESTCIV, RACACOR, SEXO, 
                                              CAUSABAS_E149, CAUSABAS_I10, CAUSABAS_I219, CAUSABAS_I64,CAUSABAS_J189]], columns=['ESC', 'ESTCIV', 'RACACOR','SEXO', 
                                                                                                                                 'CAUSABAS_E149','CAUSABAS_I10','CAUSABAS_I219','CAUSABAS_I64','CAUSABAS_J189'],
                                                                                                                                 dtype=int))
    return prediction

# "ESC","ESTCIV","RACACOR","SEXO","CAUSABAS_E149","CAUSABAS_I10","CAUSABAS_I219","CAUSABAS_I64","CAUSABAS_J189"
#st.title('**Calculadora de Longevidade**')
st.markdown("<h1 style='text-align: center;'> Calculadora de Longevidade</h1>", unsafe_allow_html=True)
image = Image.open('header.png')
st.image(image)
st.header('Digite algumas características sobre você:')
SEXO = st.selectbox('Qual o seu Sexo?', ['Masculino', 'Feminino', 'Não quero informar'])
RACACOR = st.selectbox('Qual é sua Raça/Cor?', ['Branca', 'Preta', 'Amarela', 'Parda', 'Indígena'])
ESTCIV = st.selectbox('Qual é seu Estado Civil?:', ['Solteiro', 'Casado', 'Viúvo', 'Separado judicialmente', 'União consensual', 'Não quero informar'])
ESC = st.selectbox('Por quantos anos você estudou?:', ['Não estudei formalmente', '1 a 3 anos', '4 a 7 anos', '8 a 11 anos', '12 e mais', 'Não quero informar'])
cid = st.selectbox('Qual é ou foi seu CID?:', ['CID I219 - Infarto agudo do miocárdio', 
                                          'CID I10 - Hipertensão essencial (Primária)', 
                                          'CID I64 - Acidente vascular cerebral', 
                                          'CID J189 - Pneumonia por microorganismo', 
                                          'CID E149 - Diabetes mellitus'])

CAUSABAS_E149 = 0
CAUSABAS_I10 = 0
CAUSABAS_I219 = 0
CAUSABAS_I64 = 0
CAUSABAS_J189 = 0

if st.button('Descubra a Longevidade!'):
    idade = list(predict(ESC, ESTCIV, RACACOR, SEXO, CAUSABAS_E149, CAUSABAS_I10, CAUSABAS_I219, CAUSABAS_I64,CAUSABAS_J189, cid))
    st.success(f'A longevidade para pessoas com essas características é de {idade[0]:.1f} anos')
