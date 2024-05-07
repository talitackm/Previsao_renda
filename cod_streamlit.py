import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


sns.set(context='talk', style='ticks',
        )

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon='https://assets.materialup.com/uploads/bcf6dd06-7117-424f-9a6e-4bb795c8fb4d/preview.png',
     layout="wide"
)


renda = pd.read_csv('./input/previsao_de_renda.csv')


st.title('Análise exploratória da previsão de renda')
st.subheader('')

st.write('---')

st.write('### Variáveis Qualitativas')

import altair as alt

# Criar gráficos de barra para cada categoria
charts = []
categorias = ['posse_de_imovel', 'posse_de_veiculo', 'sexo', 'tipo_renda', 'educacao', 'estado_civil', 'tipo_residencia']

for categoria in categorias:
    chart = alt.Chart(renda).mark_bar().encode(
        x=alt.X(categoria, title=None),
        y='count():Q',
        color=alt.Color(categoria, legend=None)
    ).properties(
        title=categoria,
        width=350,
        height=230
    )
    charts.append(chart)

# Organizar os gráficos em uma grade de 3 colunas e 2 linhas
rows = [alt.hconcat(*charts[i:i+3]) for i in range(0, len(charts), 3)]

# Exibir os gráficos no Streamlit
st.write(alt.vconcat(*rows), use_container_width=True)


st.write('---')
st.write('### Variáveis Quantitativas')

variables = ['qt_pessoas_residencia', 'tempo_emprego', 'idade', 'qtd_filhos']

# Criar gráficos de barra para cada variável
charts = []
for variable in variables:
    chart = alt.Chart(renda).mark_bar().encode(
        x=alt.X(variable, title=None),
        y='count():Q',
        color=alt.Color(variable, legend=None)
    ).properties(
        title=variable,
        width=540,
        height=230
    )
    charts.append(chart)

# Organizar os gráficos em uma grade de 2 colunas e 2 linhas
rows = [alt.hconcat(*charts[i:i+2]) for i in range(0, len(charts), 2)]

# Exibir os gráficos no Streamlit
st.write(alt.vconcat(*rows), use_container_width=True)
