import pandas as pd
import streamlit as st

feli = pd.read_csv("felinos_filtrado.csv")

st.title("🌿Registros De Felinos🌿")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.write(
    "Estos registros reúnen observaciones de felinos y permiten conocer mejor nuestros datos"
    "las especies encontradas, las fechas y los lugares donde fueron registradas."
)

st.image("images/Felino2.png", use_container_width=True)
st.caption("Panthera onca. Ecuador, Tungurahua, Baños. Foto por Santiago Burneo. Conocido comunmente como yaguareté en Argentina")

st.markdown("### ¿Qué es un dataset ?")
st.markdown(
    "Es un archivo que almacena muchos datos organizados en filas "
    "y columnas. Como contiene tanta información, sería complicado buscar cada dato uno "
    "por uno. Por eso, con esta web podemos filtrar la información y encontrar los datos "
    "que necesitamos de forma más rápida y sencilla."
)
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
st.header("🌿Datos interesantes del Dataset🌿")


with st.expander("¿Cuántas filas y columnas tenemos en nuestros datos?"):
    filas, columnas = feli.shape
    st.write(f"Tiene {filas} filas y {columnas} columnas.")
    st.caption("El dataset vendria a ser como un Exel que tiene ")

with st.expander("Año más antiguo y más actual"):
    st.write("Registro más antiguo:", feli["year"].min())
    st.write("Registro más actual:", feli["year"].max())
    st.caption("Al ser un Archivo descargado este esta desactualizado, para tener un registro mas actual deverian decargar el mas reciente de la Fuente oficial que parece en los datos")


with st.expander("¿Cuántas especies diferentes hay registradas en el archivo?"):
    cant = feli["species"].nunique()
    st.write(f"Tiene {cant} especies diferentes.")
    st.caption("El dataset vendria a ser como un Exel que tiene ")

with st.expander("¿Cuáles son los nombres de las columnas?"):
    columnas2 = feli.columns
    st.write("Los nombres de las columnas que tenemos son:")
    st.write(columnas2)
    st.caption("El dataset vendria a ser como un Exel que tiene ")

with st.expander("Valores nulos en el dataset"):
    valores_nulos = feli.isnull().sum()
    st.write("Datos faltantes del archivo:")
    st.write(valores_nulos)

with st.expander("¿Es verdad que Santa Cruz es la segunda provincia con más avistajes registrados?"):
    provincias = feli["stateProvince"].value_counts()
    provincias2 = provincias.head(3)
    st.write("Aquí podemos ver las tres provincias con más registros:")
    st.write(provincias2)
    st.caption("El dataset vendria a ser como un Exel que tiene ")

st.image("images/Felino1.png", use_container_width=True)

st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")