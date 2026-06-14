import streamlit as st
import joblib

# Configuração da página para remover espaços desnecessários
st.set_page_config(page_title="Fala, Comunidade!", layout="centered")

# CSS para remover o espaço vazio do topo e estilizar os cartões
st.markdown("""
    <style>
    /* Remove espaço extra do topo do Streamlit */
    .block-container { padding-top: 2rem; }
    
    /* Estilo do botão */
    div.stButton > button { 
        background-color: #2c3e50; color: white; border-radius: 10px; 
        width: 100%; height: 50px; font-weight: bold; border: none; 
    }
    
    /* Estilo dos blocos de mensagem */
    .stInfo, .stSuccess { border-radius: 15px; border-left: 5px solid #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# Título e descrição centralizados
st.title("🤖 Fala, Comunidade! 📢")
st.subheader("Seu guia para serviços públicos")
st.write("Descreva abaixo o problema que você está enfrentando. Vou te guiar passo a passo na solução.")

# Campo de entrada
texto_usuario = st.text_area("", placeholder="Ex: Estou sem energia na minha rua...", height=120)

if st.button("Buscar Solução"):
    if texto_usuario:
        with st.spinner('Analisando sua solicitação...'):
            modelo = joblib.load('modelo_ia.pkl')
            vectorizer = joblib.load('vetorizador.pkl')
            
            vetor = vectorizer.transform([texto_usuario])
            intencao = modelo.predict(vetor)[0]
            
            # Dicionário didático
            respostas = {
                "problema_energia": """
⚡ **Energia Elétrica (EDP)**
Para resolver, siga estes passos:
1. **Prepare-se:** Pegue sua conta de luz. No canto superior direito, procure pelo número chamado **'Número da Instalação'**. Você precisará dele.
2. **Teste:** Verifique se o disjuntor (aquela chave no seu quadro de energia) não caiu. Se estiver ligado e a luz não voltar, é problema na rua.
3. **Contato:** Ligue para **0800 721 0123** ou use o app 'EDP Online'.
4. **Importante:** Quando atenderem, diga seu endereço completo e o número da instalação que você anotou. Anote o número do protocolo que eles te derem!
""",
                "problema_saneamento": """
🚰 **Água e Esgoto (Sabesp)**
Vamos resolver:
1. **Teste:** Verifique se o registro de entrada de água (geralmente perto do cavalete) está totalmente aberto. 
2. **Contato:** Ligue para **0800 055 0195**.
3. **Documento:** Tenha em mãos o **'RGI'** ou **'Número do Imóvel'** que consta no topo da sua conta de água.
4. **Atenção:** Explique se é falta de água, vazamento na rua ou esgoto. Peça e anote o número do protocolo de atendimento. Sem ele, não conseguimos cobrar uma solução depois.
""",
                "acionar_ouvidoria": """
📢 **Ouvidoria Municipal**
A Ouvidoria é a nossa última esperança quando as empresas não resolvem.
1. **O que precisa:** Você só pode acionar a ouvidoria se já tiver tentado falar com a empresa (EDP ou Sabesp) e eles não resolveram.
2. **Documento:** Você precisa obrigatoriamente do **número do protocolo** da reclamação anterior.
3. **Como fazer:** Acesse o site da Prefeitura de SJC ou vá presencialmente ao Paço Municipal. Diga: 'Já tenho o protocolo X e não resolveram, quero formalizar uma queixa na Ouvidoria'.
""",
                "agencia_reguladora": """
⚖️ **Órgão Regulador (ANEEL ou ARSESP)**
Se nem a empresa nem a ouvidoria ajudaram, vamos para quem manda nelas:
1. **Quem procurar:** Para luz é a **ANEEL**; para água é a **ARSESP**.
2. **Documento:** Junte todas as contas e todos os números de protocolo que você anotou nas ligações anteriores.
3. **Ação:** Entre no site oficial dessas agências. Eles são os fiscais que aplicam multas nas empresas. Eles vão precisar da sua reclamação bem detalhada com os protocolos anteriores.
"""
            }
            
            st.success("Encontrei o caminho para você:")
            st.info(respostas.get(intencao, "Desculpe, não consegui identificar uma categoria específica. Tente descrever com mais detalhes."))
    else:
        st.warning("Por favor, digite uma reclamação.")

st.markdown("---")
st.caption("<center>Projeto de Extensão - UNIVAP | Apoio ao Cidadão</center>", unsafe_allow_html=True)