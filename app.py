import streamlit as st
import joblib

# Carregar o modelo e o vetorizador que você acabou de criar
modelo = joblib.load('modelo_ia.pkl')
vectorizer = joblib.load('vetorizador.pkl')

st.title("Fala, Comunidade! 📢")
st.write("Como posso te ajudar hoje?")

texto = st.text_input("Digite sua reclamação:")

if st.button("Enviar"):
    # Transformar o texto do usuário
    texto_vetorizado = vectorizer.transform([texto])
    # Fazer a previsão
    previsao = modelo.predict(texto_vetorizado)
    st.success(f"Intenção detectada: {previsao[0]}")