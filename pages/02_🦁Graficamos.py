import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
feli = pd.read_csv("felinos_filtrado.csv")

st.title("🌿Gráficos De Avistamientos🌿")
st.write("Los gráficos nos permiten representar los datos de una forma visual y fácil de entender. El gráfico de barras sirve para comparar cantidades, el gráfico de torta para mostrar porcentajes y el gráfico de líneas para observar cómo cambian los datos a lo largo del tiempo. Gracias a ellos, podemos analizar la información y comprender mejor los resultados.")
st.image("images/H.png", use_container_width=True)
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")


# Avistamientos por mes durante 2010
feli_2010 = feli[feli["year"] == 2010]
meses_2010 = feli_2010["month"].value_counts().sort_index()

fig = px.line(
    x=meses_2010.index,
    y=meses_2010.values,
    title="Cantidad de avistamientos por mes en 2010",
    labels={"x": "Mes", "y": "Cantidad de avistamientos"},
    markers=True
)

# Avistamientos por mes en todo el dataset
meses = feli["month"].value_counts().sort_index()

fig2 = px.bar(
    x=meses.index,
    y=meses.values,
    title="Cantidad de avistamientos por mes",
    labels={"x": "Mes", "y": "Cantidad de avistamientos"}
)

nombres_meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

porcentajes = meses / meses.sum() * 100

fig3 = px.pie(
    values=meses.values,
    names=meses.index.map(nombres_meses),
    title="Porcentaje de avistamientos por mes"
)

# Avistamientos por mes en el año más reciente del dataset
anio_actual = feli["year"].max()
feli_actual = feli[feli["year"] == anio_actual]
meses_actual = feli_actual["month"].value_counts().sort_index()

fig4 = px.line(
    x=meses_actual.index,
    y=meses_actual.values,
    title=f"Avistamientos por mes en {anio_actual}",
    labels={"x": "Mes", "y": "Cantidad de avistamientos"},
    markers=True
)

# Avistamientos por provincia
provincias = feli["stateProvince"].value_counts()

fig5 = px.bar(
    x=provincias.index,
    y=provincias.values,
    title="Cantidad de avistamientos por provincia",
    labels={"x": "Provincia", "y": "Cantidad de avistamientos"}
)

st.plotly_chart(fig, use_container_width=True)
st.caption("Este gráfico de líneas muestra cómo variaron los avistamientos durante los meses de 2010 y permite comparar los registros de cada mes.")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.plotly_chart(fig4, use_container_width=True)
st.caption(f"Este gráfico muestra los avistamientos de cada mes del año más reciente disponible en el dataset ({anio_actual}), para observar cómo se distribuyeron durante ese año.")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.plotly_chart(fig2, use_container_width=True)
st.caption("Este gráfico de barras compara la cantidad total de avistamientos registrados en cada mes, considerando todos los años incluidos en el dataset.")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.plotly_chart(fig5, use_container_width=True)
st.caption("Este gráfico compara los registros entre provincias y permite identificar en cuáles se concentró la mayor cantidad de avistamientos.")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.plotly_chart(fig3, use_container_width=True)
st.caption("Este gráfico circular representa qué porcentaje del total de avistamientos corresponde a cada mes. Así se pueden comparar las proporciones mensuales.")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
st.image("images/Felino3.png", use_container_width=True)
