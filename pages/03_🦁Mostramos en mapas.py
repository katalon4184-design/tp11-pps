import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

#no tocar

def generar_mapa():

    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )

    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'

    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )

    return m


# Cargar el dataset
feli = pd.read_csv("felinos_filtrado.csv")

st.title("Mapa de felinos de Argentina")
st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
st.image("images/M.png", use_container_width=True)


# ============================================================
# Limpiar registros sin coordenadas
# dropna() elimina las filas que tienen valores vacíos.
# subset=["lat", "lng"] indica que solamente queremos eliminar filas que tengan vacía la latitud o la longitud.
# .copy() crea una copia independiente de los datos filtrados.
# ============================================================

feli = feli.dropna(subset=["lat", "lng"]).copy()

# Obtener las especies disponibles
especies = sorted(feli["species"].dropna().unique())

# Crear el selector
opciones = ["Todas las especies"] + especies

especie_seleccionada = st.selectbox(
    "Seleccioná una especie de felino:",
    opciones
)

# Filtrar según la selección

if especie_seleccionada == "Todas las especies":
    felinos_mostrar = feli
else:
    felinos_mostrar = feli[
        feli["species"] == especie_seleccionada
    ]

# Crear el mapas
mapa_felinos = generar_mapa()

# Agregar los marcadores
for _, row in felinos_mostrar.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=f"Especie: {row['species']}",
        tooltip=row["species"],
        icon=folium.Icon(
            color="blue",
            icon="paw",
            prefix="fa"
        )
    ).add_to(mapa_felinos)

# Mostrar cantidad de registros
st.write(
    "Ubicaciones mostradas:",
    len(felinos_mostrar)
)

# Mostrar el mapa
st_folium(
    mapa_felinos,
    width=900,
    height=600,
    key="mapa_felinos"
)

st.write("Especies encontradas:")
st.write(feli["species"].value_counts())

st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
st.image("images/Felino4.png", use_container_width=True)