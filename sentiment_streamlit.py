import streamlit as st
import requests
from loguru import logger
from sys import stderr

logger.add(stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("logs/sentiment_streamlit.log")

logger.debug("L'application Streamlit est en cours de démarrage...")

st.header("Analyse de sentiment")

with st.form("my_form"):
    st.write("Saisissez un texte pour analyser le sentiment.")
    text = st.text_area("Entrez un texte pour analyser le sentiment.")
    submitted = st.form_submit_button("Envoyer")

    if submitted:
        response = requests.post("http://127.0.0.1:80/analyse_sentiment/", json={"text": text})
        response.raise_for_status() 
        sentiment = response.json()

        st.text(sentiment["raw"])
        st.text(sentiment["interpretation"]["label"])
        st.text(sentiment["interpretation"]["emoji"])
