import streamlit as st
import base64
import streamlit.components.v1 as components

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

@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Oxanium:wght@300;400;600&display=swap');

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

.block-container {
    max-width: 900px;
    margin: auto;
}

* {
    font-family: 'Oxanium', sans-serif !important;
}

.stButton>button {
    font-size: 15px;
    border-radius: 10px;
    width: 100%;
}

/* 🔥 BOTÃO DO MENU: remove keyboard_... e mostra ☰ */
button[kind="header"] {
    font-size: 0 !important;
    background-color: #11A17E !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 8px 12px !important;
    transition: 0.3s;
    box-shadow: 0 4px 10px rgba(0,0,0,0.25) !important;
}

button[kind="header"]::after {
    content: "☰";
    font-size: 26px !important;
    color: white !important;
}

button[kind="header"]:hover {
    background-color: #0d8a6a !important;
}

/* ==============================
SIDEBAR CUSTOM 🔥
============================== */

section[data-testid="stSidebar"] {
    background-color: #11A17E !important;
}

section[data-testid="stSidebar"] * {
    font-family: 'Oxanium', sans-serif !important;
    color: white !important;
}

section[data-testid="stSidebar"] h2 {
    font-family: 'Audiowide', sans-serif !important;
    font-size: 22px !important;
    letter-spacing: 1px;
    text-align: center !important;
}

section[data-testid="stSidebar"] .stAlert {
    background-color: rgba(0,0,0,0.22) !important;
    border-radius: 12px !important;
    border: none !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# LOGO + TÍTULO CENTRALIZADOS
# ==============================
def carregar_logo(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = carregar_logo("logo.png")

components.html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Oxanium:wght@300;400;600&display=swap');

.header-agro {{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

.logo-agro {{
    width: 140px;
    height: auto;
    margin-bottom: 12px;
}}

.titulo-agro {{
    font-family: 'Audiowide', sans-serif;
    font-size: 38px;
    color: white;
    text-align: center;
}}

.subtitulo-agro {{
    font-family: 'Oxanium', sans-serif;
    font-size: 20px;
    color: #cccccc;
    text-align: center;
}}

@media (max-width: 768px) {{
    .titulo-agro {{
        font-size: 26px;
    }}

    .subtitulo-agro {{
        font-size: 16px;
    }}
}}
</style>

<div class="header-agro">
    <img class="logo-agro" src="data:image/png;base64,{logo_base64}">
    <div class="titulo-agro">AgroSmart PRO</div>
    <div class="subtitulo-agro">Tecnologia aplicada ao agronegócio</div>
</div>
""", height=240)

# ==============================
# SIDEBAR
# ==============================
st.sidebar.markdown("## 🌱 AgroSmart PRO")
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
