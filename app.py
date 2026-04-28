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

/* 🔥 TROCAR keyboard_... por Menu */

/* esconde texto original */
button[kind="header"] span,
button[kind="header"] p {
    visibility: hidden !important;
}

/* adiciona "Menu" */
button[kind="header"]::after {
    content: "Menu";
    visibility: visible;
    font-size: 16px;
    color: white;
}

/* estilo botão */
button[kind="header"] {
    background-color: #11A17E !important;
    border-radius: 10px !important;
    padding: 6px 12px !important;
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
# LOGO + TÍTULO
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
