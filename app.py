import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# Título y descripción
st.title('Análisis de Sentimientos con TextBlob')
st.write("Esta aplicación analiza la polaridad y subjetividad de un texto en español o inglés.")

# Sidebar con información
with st.sidebar:
    st.subheader("¿Cómo funciona el análisis?")
    st.markdown("""
    **Polaridad:** 
    - Rango de -1 (muy negativo) a 1 (muy positivo).
    - 0 es neutral.

    **Subjetividad:**  
    - Rango de 0 (hechos) a 1 (opiniones/emociones).
    """)
    st.markdown("---")
    st.write("💡 Consejo: El análisis funciona mejor en inglés, se traducirá automáticamente.")

# Secciones con Tabs
tab1, tab2 = st.tabs(["📊 Analizar Sentimiento", "📝 Corrección de Texto"])

# --- TAB 1: Análisis de Sentimiento ---
with tab1:
    text = st.text_area("✍️ Escribe una frase para analizar:")

    if text:
        try:
            translation = translator.translate(text, src="es", dest="en")
            trans_text = translation.text
            blob = TextBlob(trans_text)

            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)

            st.write(f"🔹 **Polaridad:** {polarity}")
            st.write(f"🔹 **Subjetividad:** {subjectivity}")

            # Variaciones en el análisis
            if polarity > 0.5:
                st.success("😊 El sentimiento es **muy positivo**.")
            elif 0.1 < polarity <= 0.5:
                st.success("🙂 El sentimiento es **ligeramente positivo**.")
            elif -0.1 <= polarity <= 0.1:
                st.info("😐 El sentimiento es **neutral**.")
            elif -0.5 < polarity < -0.1:
                st.warning("🙁 El sentimiento es **ligeramente negativo**.")
            else:
                st.error("😔 El sentimiento es **muy negativo**.")

        except Exception as e:
            st.error(f"❌ Error en la traducción o análisis: {e}")

# --- TAB 2: Corrección en Inglés ---
with tab2:
    text2 = st.text_area("✍️ Escribe una frase en inglés para corregir:", key="correct_text")
    
    if text2:
        blob2 = TextBlob(text2)
        st.write("✏️ **Corrección sugerida:**")
        st.success(blob2.correct())
