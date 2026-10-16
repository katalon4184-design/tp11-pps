import pandas as pd
import streamlit as st

feli =  pd.read_csv('felinos_filtrado.csv')

st.title("Datos De Los Registros De Felinos")
st.header("Informacion:")

with st.expander("¿Cuántas Filas y columas hay en el archivo?"):
    filas, colum = feli.shape
    st.write(f'Tiene {filas} filas y {colum} columnas')
    
with st.expander("Año mas antiguo y mas actual"):    
    st.write("Registro más antiguo:", feli["year"].min())
    st.write("Registro más actual:", feli["year"].max())

with st.expander("¿Cuántas especies diferentes hay registradas en el archivo?"):
    cant = feli["species"].nunique()
    st.write(f'Tiene {cant} especies diferentes.')

with st.expander("¿cuales son los nombres de las columnas?"):
    colum2 = feli.columns
    st.write("los nombres de las columnas que tenemos son:")
    st.write(colum2)

with st.expander("Valores nulos en el dataset"):
    M =feli.isnull().sum()
    st.write(f'datos faltantes del archivo:')
    st.write (M)
    
with st.expander("¿Es verdad que Santa Cruz es la segunda provincia con más avistajes registrados?"):
    provin = feli["stateProvince"].value_counts() 
    provin2 = provin.head(3)
    st.write(f'Aqui podemos ver que si es verdad:')
    st.write(provin2)
   
   

        