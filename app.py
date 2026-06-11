import streamlit as st
import joblib

# Carregar o modelo e o vetorizador que você treinou
# Certifique-se de que esses arquivos estão na mesma pasta que o app.py
modelo = joblib.load('modelo_ia.pkl')
vectorizer = joblib.load('vetorizador.pkl')

st.title("🤖 Fala, Comunidade!")
st.write("Assistente inteligente para suporte a serviços públicos.")

# Campo de entrada do usuário
texto_usuario = st.text_input("Descreva o seu problema (ex: estou sem energia na minha rua):")

if st.button("Buscar Solução"):
    if texto_usuario:
        # Traduzir o texto para o formato que a IA entende
        vetor = vectorizer.transform([texto_usuario])
        
        # Fazer a previsão da intenção
        resultado = modelo.predict(vetor)
        intencao = resultado[0]
        
        # Dicionário de respostas orientativas (O coração do projeto)
        respostas = {
           "problema_energia": "⚡ **Entendi que você está enfrentando um problema relacionado à energia elétrica.**\n\nPara resolver a situação o mais rápido possível, entre em contato com a EDP São José dos Campos pelo telefone **0800 721 0123** ou pelo aplicativo **EDP Online**.\n\nAntes de iniciar o atendimento, tenha em mãos o número da instalação (código que aparece na sua conta de luz), pois isso ajuda a localizar seu cadastro com mais agilidade.\n\nCaso já tenha realizado um contato anterior, guarde também o número do protocolo para acompanhar a solicitação.",
           "problema_saneamento": "🚰 **Identifiquei que sua solicitação está relacionada ao abastecimento de água ou saneamento.**\n\nO primeiro passo é entrar em contato com a Sabesp pelo telefone **0800 055 0195** ou pelos canais digitais oficiais da empresa.\n\nDurante o atendimento, explique o problema com o máximo de detalhes possível e anote o número do protocolo fornecido.\n\nSe a situação não for resolvida dentro do prazo informado ou se você não receber retorno em até 24 horas, o protocolo será importante para registrar uma nova manifestação junto aos órgãos responsáveis.",
           "acionar_ouvidoria": "📢 **Você deseja registrar uma manifestação na Ouvidoria.**\n\nA Ouvidoria é o canal responsável por analisar casos que não foram solucionados pelos atendimentos convencionais.\n\nAntes de abrir sua solicitação, verifique se você possui o número do protocolo do atendimento anterior, pois ele normalmente será solicitado durante o registro.\n\nCom essas informações em mãos, acesse o portal da Ouvidoria Municipal de São José dos Campos e descreva o ocorrido de forma clara para facilitar a análise do seu caso.",
           "agencia_reguladora": "⚖️ **Caso a empresa responsável não tenha solucionado o problema, existem órgãos reguladores que podem ajudar.**\n\nPara questões relacionadas ao abastecimento de água e saneamento, você pode registrar uma reclamação na **ARSESP**. Já para problemas envolvendo energia elétrica, o órgão responsável é a **ANEEL**.\n\nEssas instituições fiscalizam a qualidade dos serviços prestados e podem acompanhar situações em que a concessionária não apresentou uma solução adequada.\n\nTenha em mãos seus protocolos de atendimento e documentos relacionados à ocorrência para agilizar o processo."
        }
        
        # Exibição do resultado
        st.success(f"Classificação do sistema: {intencao}")
        st.info(respostas.get(intencao, "Não consegui identificar uma categoria específica para este relato. Tente descrever com mais detalhes como 'falta de água' ou 'luz piscando'."))
    else:
        st.warning("Por favor, digite uma reclamação para que eu possa te ajudar.")