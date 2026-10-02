import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
feli = pd.read_csv('felinos_filtrado.csv')

# Título de la página
st.title("Graficos")

# Crear el gráfico
feli_2010 = feli[feli["year"] == 2010]
meses_2010 = feli_2010["month"].value_counts().sort_index()

fig = px.line(
    x=meses_2010.index,
    y=meses_2010.values,
    title="Cantidad de avistamientos por mes en 2010",
    labels={"x": "Mes", "y": "Cantidad de avistamientos"},
    markers=True
)

# Mostrar el gráfico
st.plotly_chart(fig)