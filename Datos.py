import streamlit as st

st.image("images/banner.png", use_container_width=True)

st.title("Análisis de datos de felinos de Argentina 🐆")
st.subheader("Con Python 🐍 y un dataset de registros de felinos 🌿")

st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.write(
    """
    Argentina cuenta con distintas especies de felinos que viven en zonas variadas,
    desde selvas y montes hasta zonas de pastizales y regiones patagónicas. Conocer dónde
    aparecen y cuándo fueron registrados nos ayuda a entender mejor su presencia y a reconocer
    la importancia de proteger sus hábitats.
    """
)

st.write(
    "En esta web exploramos registros de felinos para descubrir qué especies tenemos en la argentina y cuales de estas son mas frecuentes, "
    "en qué provincias se concentran los avistamientos y cómo se distribuyen a lo largo del tiempo."
)

st.write("⬇️ Consultá la fuente original de los datos:")
st.page_link("https://www.gbif.org/", label="Fuente del dataset: GBIF")
