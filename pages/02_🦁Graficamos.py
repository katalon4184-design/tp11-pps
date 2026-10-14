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

#Grafico de barra
meses = feli["month"].value_counts().sort_index()

fig2 = px.bar(
    x=meses.index,
    y=meses.values,
    title="Cantidad de avistamientos por mes",
    labels={"x": "Mes", "y": "Cantidad de avistamientos"}
)

##torta

meses = feli["month"].value_counts().sort_index()

porcentajes = meses / meses.sum() * 100

fig3 = px.pie(
    values=meses.values,
    names=meses.index,
    title="Porcentaje de avistamientos por mes"
)


# Mostrar el gráfico

st.plotly_chart(fig)
st.plotly_chart(fig2)
st.plotly_chart(fig3)