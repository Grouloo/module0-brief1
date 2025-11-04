import streamlit as st
import requests

response = requests.post("http://127.0.0.1:80/analyse_sentiment/", json={"text": "Hello World"})
response.raise_for_status() 
sentiment = response.json()

st.header("Analyse de sentiment")

st.text_area("Entrez un texte pour analyser le sentiment.")

st.text(sentiment["raw"])

st.text(sentiment["interpretation"]["label"])
st.text(sentiment["interpretation"]["emoji"])