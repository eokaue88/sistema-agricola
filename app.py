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
# CSS + RESPONSIVIDADE
# ==============================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Oxanium:wght@300;400;600&display=swap');

.stApp {
    background: radial-gradient(circle at top, #23306b 0%, #171B48 45%, #090b1f 100%);
}

.block-container {
    max-width: 1050px;
    margin: auto;
    padding-top: 2rem;
}

.stApp,
.stApp p,
.stApp label,
.stApp div,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6,
.stButton button,
.stSelectbox * {
    font-family: 'Oxanium', sans-serif !important;
}

.stButton>button {
    background: linear-gradient(90deg, #11A17E, #18d6a6);
    color: white;
    font-weight: 700;
    border: none;
    border-radius: 14px;
    height: 3.4em;
    box-shadow: 0 8px 22px rgba(17,161,126,0.35);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 12px 30px rgba(17,161,126,0.6);
}

.stSelectbox>div>div {
    background: rgba(255,255,255,0.08);
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.2);
}

section[data-testid="stSidebar"] {
    background-color: #11A17E !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {
    font-family: 'Oxanium', sans-serif !important;
    color: white !important;
}

section[data-testid="stSidebar"] h2 {
    font-family: 'Audiowide', sans-serif !important;
    font-size: 22px !important;
    text-align: center !important;
}

.card-agro {
    background: linear-gradient(160deg, rgba(255,255,255,0.12), rgba(255,255,255,0.04));
    backdrop-filter: blur(12px);
    padding: 24px;
    border-radius: 22px;
    color: white;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    transition: 0.35s;
    min-height: 180px;
}

.card-agro:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 20px 50px rgba(17,161,126,0.5);
}

.card-top1 {
    background: linear-gradient(160deg, #11A17E, #064c3e);
    border: 2px solid rgba(255,255,255,0.5);
    transform: scale(1.02);
}

.card-agro h3 {
    font-size: 24px;
    margin-bottom: 10px;
}

.card-agro h2 {
    font-size: 34px;
    margin: 8px 0;
}

.card-agro p {
    font-size: 15px;
    opacity: 0.9;
}

[data-testid="stVerticalBlock"] {
    gap: 1.2rem;
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
    width: 110px;
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
""", height=190)

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

    st.markdown(f"""
    <div class="card-agro card-top1">
        <p>🎯 Melhor escolha para sua fazenda</p>
        <h3>{melhor[0].upper()}</h3>
        <p>Compatibilidade geral</p>
        <h2>{melhor[1]:.0f}%</h2>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("## 🌾 Ranking de culturas recomendadas")

    cols = st.columns(3)

    for i, (cultura, porc) in enumerate(resultados[:6]):
        with cols[i % 3]:

            classe_extra = "card-top1" if i == 0 else ""

            st.markdown(f"""
            <div class="card-agro {classe_extra}">
                <p>#{i+1} recomendação</p>
                <h3>{cultura.upper()}</h3>
                <p>🌱 Compatibilidade</p>
                <h2>{porc:.0f}%</h2>
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(porc))
