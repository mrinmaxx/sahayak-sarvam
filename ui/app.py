import streamlit as st
import tempfile
import os
from config.languages import LANGUAGES
from core.pipeline import run

st.set_page_config(page_title="Sahayak", layout="centered")
st.title("Sahayak: Multilingual Voice Agent")

lang = st.selectbox("Choose your language", list(LANGUAGES.keys()), format_func=lambda c: LANGUAGES[c])
audio_file = st.audio_input("Record your question")

if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        audio_path = tmp.name
    with st.spinner("Processing..."):
        try:
            result = run(audio_path, lang)
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()
    os.unlink(audio_path)
    st.write("**Transcript:**", result["transcript"])
    st.write("**Response:**", result["response"])
    if result["audio"]:
        st.audio(result["audio"], format="audio/wav")
