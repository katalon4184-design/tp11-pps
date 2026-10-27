import streamlit as st

st.set_page_config(page_title="Juego de Preguntas", page_icon="🎮🌿")
st.title("🌿🎮 Juego de Preguntas 🎮🌿")

st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")

st.image("images/T.png", use_container_width=True)

# ============================================================
# Definimos las preguntas
# ============================================================
preguntas = [
    {
        "pregunta": "¿Cuántas especies diferentes tenemos?",
        "opciones": ["10", "9", "8"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuál fue la segunda provincia con más avistajes?",
        "opciones": ["Formosa", "Misiones", "Santa Cruz"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuántos registros se tienen de la Panthera onca?",
        "opciones": ["334", "172", "237"],
        "correcta": 1
    },
]

# ============================================================
# Una pregunta por bloque, con su propio botón de verificar
# ============================================================
for i, p in enumerate(preguntas):
    st.subheader(f"• Pregunta {i + 1} •")
    st.write(p["pregunta"])

    # El radio guarda la elección del estudiante
    eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    # Cada pregunta tiene su propio botón
    if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.balloons()
            st.success("✅ ¡Correcto!")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"❌ Incorrecto. ¡No te preocupes vuelve a intentarlo!")

    st.divider()
    st.header(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    
st.image("images/Felino2.png", use_container_width=True)