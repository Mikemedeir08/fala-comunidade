import streamlit as st
import joblib

# Configurações globais para um visual "App"
st.set_page_config(page_title="Fala, Comunidade!", layout="centered")

# Estilização para um visual limpo (UI de cartão)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .css-1r6slp0 { padding-top: 2rem; }
    div.stButton > button:first-child {
        background-color: #2c3e50; color: white; border-radius: 10px;
        width: 100%; height: 50px; font-weight: bold; border: none;
    }
    div.stButton > button:hover { background-color: #34495e; }
    .card {
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Conteúdo principal
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("🤖 Fala, Comunidade! 📢")
st.subheader("Como podemos ajudar hoje?")
st.write("Descreva o seu problema e indicaremos o melhor caminho oficial para a solução.")

texto_usuario = st.text_area("", placeholder="Ex: Estou sem energia na minha rua...", height=120)

if st.button("Buscar Solução"):
    if texto_usuario:
        # Carregamento do modelo (se necessário, coloque fora do loop em produção)
        modelo = joblib.load('modelo_ia.pkl')
        vectorizer = joblib.load('vetorizador.pkl')
        
        vetor = vectorizer.transform([texto_usuario])
        intencao = modelo.predict(vetor)[0]
        
        # Mapeamento de soluções
        respostas = {
            "problema_energia": "⚡ **Energia Elétrica**\n\nEntre em contato com a EDP São José dos Campos pelo telefone 0800 721 0123 ou pelo app 'EDP Online'. Tenha em mãos o número da instalação.",
            "problema_saneamento": "🚰 **Saneamento e Água**\n\nEntre em contato com a Sabesp pelo telefone 0800 055 0195. Se não resolvido em 24h, use o protocolo para acionar a ouvidoria.",
            "acionar_ouvidoria": "📢 **Ouvidoria Municipal**\n\nEste é o canal para casos não resolvidos. Tenha seu protocolo em mãos e acesse o portal oficial da prefeitura de SJC.",
            "agencia_reguladora": "⚖️ **Órgão Regulador**\n\nPara conflitos não solucionados, registre sua queixa na ANEEL (energia) ou ARSESP (água). Eles fiscalizam a prestação do serviço."
        }
        
        st.markdown("---")
        st.info(respostas.get(intencao, "Não consegui identificar a categoria. Tente ser mais específico."))
    else:
        st.warning("Por favor, digite o seu problema.")
st.markdown("</div>", unsafe_allow_html=True)

st.caption("<center>Projeto de Extensão - UNIVAP | Apoio ao Cidadão</center>", unsafe_allow_html=True)