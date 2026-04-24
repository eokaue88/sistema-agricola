import streamlit as st

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="AgroSmart PRO",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# CSS + RESPONSIVIDADE 🔥
# ==============================
st.markdown("""
<style>

/* FONTES */
@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Oxanium:wght@300;400;600&display=swap');

/* FUNDO */
.stApp {
    background-color: #171B48;
}

.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.3);
    z-index: -1;
}

/* CONTAINER */
.block-container {
    max-width: 900px;
    margin: auto;
}

/* 🔥 FONTE GLOBAL FORÇADA */
* {
    font-family: 'Oxanium', sans-serif !important;
}

/* TÍTULO */
.titulo-agro {
    font-family: 'Audiowide', sans-serif !important;
    font-size: 38px;
    text-align: center;
    color: white;
}

/* SUBTÍTULO */
.subtitulo-agro {
    font-size: 20px;
    text-align: center;
    color: #cccccc;
}

/* BOTÃO */
.stButton>button {
    font-size: 15px;
    border-radius: 10px;
    width: 100%;
}

/* CARDS */
.card-agro {
    font-size: 15px;
}

/* 🔥 RESPONSIVO */
@media (max-width: 768px) {

    .titulo-agro {
        font-size: 26px;
    }

    .subtitulo-agro {
        font-size: 16px;
    }

    img {
        width: 120px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ==============================
# LOGO + TÍTULO (PERFEITO 🔥)
# ==============================
st.markdown("""
<div style="text-align:center;">

    <img src="logo.png" style="
        width:160px;
        display:block;
        margin-left:auto;
        margin-right:auto;
    ">

    <div class="titulo-agro">
        AgroSmart PRO
    </div>

    <div class="subtitulo-agro">
        Tecnologia aplicada ao agronegócio
    </div>

    <br>

</div>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("🌱 AgroSmart PRO")
st.sidebar.info("Sistema inteligente de recomendação agrícola")

# ==============================
# BASE
# ==============================
dados = [
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "cultura": "soja"},
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "cultura": "milho"},
    {"solo": "argiloso", "clima": "umido", "regiao": "sul", "cultura": "arroz"},
    {"solo": "argiloso", "clima": "frio", "regiao": "sul", "cultura": "trigo"},
    {"solo": "misto", "clima": "quente", "regiao": "sudeste", "cultura": "feijao"},
    {"solo": "argiloso", "clima": "ameno", "regiao": "sudeste", "cultura": "cafe"},
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "cultura": "algodao"},
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "cultura": "mandioca"},
    {"solo": "argiloso", "clima": "umido", "regiao": "sudeste", "cultura": "tomate"},
]

# ==============================
# INPUTS
# ==============================
st.subheader("📥 Dados da propriedade")

col1, col2, col3 = st.columns(3)

with col1:
    solo = st.selectbox("🌍 Solo", ["arenoso", "argiloso", "misto"])

with col2:
    clima = st.selectbox("☁️ Clima", ["quente", "umido", "seco", "frio", "ameno", "tropical"])

with col3:
    regiao = st.selectbox("📍 Região", ["nordeste", "sul", "sudeste", "norte", "centro-oeste"])

# ==============================
# BOTÃO
# ==============================
if st.button("🚀 Gerar recomendação"):

    resultados = []

    for item in dados:
        pontuacao = 0

        if item["solo"] == solo:
            pontuacao += 1
        if item["clima"] == clima:
            pontuacao += 2
        if item["regiao"] == regiao:
            pontuacao += 1

        porcentagem = (pontuacao / 4) * 100
        resultados.append((item["cultura"], porcentagem))

    resultados.sort(key=lambda x: x[1], reverse=True)
    melhor = resultados[0]

    st.markdown("## 🎯 Melhor escolha para sua fazenda")

    st.success(f"""
    🌱 **{melhor[0].upper()}**
    📊 Compatibilidade: **{melhor[1]:.0f}%**
    """)

    st.divider()

    st.subheader("📈 Comparação")
    valores = [c[1] for c in resultados]
    st.bar_chart(valores)

    st.divider()

    st.markdown("## 🍿 Recomendações")

    cols = st.columns(3)

    for i, (cultura, porc) in enumerate(resultados[:6]):
        with cols[i % 3]:

            st.markdown(f"""
            <div class="card-agro" style="
                background-color: {'#2e7d32' if i == 0 else '#333'};
                padding: 12px;
                border-radius: 12px;
                text-align: center;
                color: white;
            ">
                <h3>{cultura.upper()}</h3>
                <p>{porc:.0f}%</p>
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(porc))

    st.divider()

    st.subheader("🏆 Ranking")
    for i, (cultura, porc) in enumerate(resultados[:5], start=1):
        st.write(f"{i}º — {cultura} ({porc:.0f}%)")

    st.divider()

    st.subheader("🧠 Análise")

    if melhor[1] >= 75:
        st.success("Alta compatibilidade")
    elif melhor[1] >= 50:
        st.info("Compatibilidade média")
    else:
        st.warning("Baixa compatibilidade")
