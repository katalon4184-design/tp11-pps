import pandas as pd
import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background-color: #0B0B0B;
    }
    </style>
    """, unsafe_allow_html=True)

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
    st.caption("Esta información nos permite conocer el tamaño del dataset y saber cuántos registros y datos contiene.")

with st.expander("Año más antiguo y más actual que se vio un felino"):
    st.write("Registro más antiguo:", int(feli["year"].min()))
    st.write("Registro más actual:", int(feli["year"].max()))
    st.caption("Nos permite conocer el período de tiempo que abarcan los registros y analizar desde qué año hasta cuál se tienen datos de avistamientos.")


with st.expander("¿Cuántas especies diferentes hay registradas en el archivo?"):
    cant = feli["species"].nunique()
    st.write(f"Tiene {cant} especies diferentes.")
    st.caption("Nos permite saber cuánta variedad de felinos se encuentra representada en el dataset.")

with st.expander("¿Cuales son los nombres de los felinos guardados?"):
    st.write("Nombres:")
    st.write(feli["species"].value_counts())
    st.caption("Nos permite identificar qué especies están incluidas en los registros y conocer cuáles son los felinos estudiados.")

with st.expander("¿Cuáles son los nombres de las columnas?"):
    columnas2 = feli.columns
    st.write("Los nombres de las columnas que tenemos son:")
    st.write(columnas2)
    st.caption("Nos ayuda a reconocer qué tipo de información contiene el archivo y qué datos podemos utilizar para realizar los análisis.")

with st.expander("Valores nulos en el dataset"):
    valores_nulos = feli.isnull().sum()
    st.write("Datos faltantes del archivo:")
    st.caption("Nos permite identificar qué datos están incompletos y conocer si hay información faltante que pueda afectar los análisis.")
    st.write(valores_nulos)

with st.expander("¿Cuales son las 3 provincias con más avistajes registrados?"):
    provincias = feli["stateProvince"].value_counts()
    provincias2 = provincias.head(3)
    st.write("Aquí podemos ver las tres provincias con más registros:")
    st.write(provincias2)
    st.caption("Nos permite identificar en qué provincias se concentra la mayor cantidad de avistamientos y conocer cuáles tienen más registros de felinos.")

st.image("images/Felino1.png", use_container_width=True)

st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")