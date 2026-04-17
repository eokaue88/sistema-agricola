import streamlit as st

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="AgroSmart PRO",
    page_icon="🌱",
    layout="wide"
)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=260)

st.markdown("""
<style>
body {
    background-color: #0e1117;
}

/* Centralizar conteúdo */
.block-container {
    max-width: 900px;
    margin: auto;
}

/* Botão */
.stButton>button {
    background-color: #2e7d32;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

/* Selectbox */
.stSelectbox>div>div {
    background-color: #1e1e1e;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("🌱 AgroSmart PRO")
st.sidebar.info("Sistema inteligente de recomendação agrícola")

# ==============================
# TÍTULO
# ==============================
st.title("🌱 AgroSmart PRO")
st.caption("Tecnologia aplicada ao agronegócio")

# ==============================
# BASE DE DADOS
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
# BOTÃO (CORRIGIDO)
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

    # ==============================
    # 🎯 DESTAQUE PRINCIPAL
    # ==============================
    st.markdown("## 🎯 Melhor escolha para sua fazenda")

    st.success(f"""
    🌱 **{melhor[0].upper()}**

    📊 Compatibilidade: **{melhor[1]:.0f}%**
    """)

    st.divider()

    # ==============================
    # GRÁFICO
    # ==============================
    st.subheader("📈 Comparação")

    valores = [c[1] for c in resultados]
    st.bar_chart(valores)

    st.divider()

    # ==============================
    # CARDS (ESTILO NETFLIX)
    # ==============================
    st.markdown("## 🍿 Recomendações para você")

    cols = st.columns(3)

    for i, (cultura, porc) in enumerate(resultados[:6]):
        with cols[i % 3]:
            cor = "#2e7d32" if i == 0 else "#333"

            st.markdown(f"""
            <div style="
                background-color: {cor};
                padding: 15px;
                border-radius: 15px;
                color: white;
                text-align: center;
            ">
                <h3>{cultura.upper()}</h3>
                <p>{porc:.0f}% compatível</p>
                <p>#{i+1}</p>
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(porc))

    st.divider()

    # ==============================
    # RANKING
    # ==============================
    st.subheader("🏆 Ranking")

    for i, (cultura, porc) in enumerate(resultados[:5], start=1):
        st.write(f"{i}º — {cultura} ({porc:.0f}%)")

    st.divider()

    # ==============================
    # ANÁLISE
    # ==============================
    st.subheader("🧠 Análise")

    if melhor[1] >= 75:
        st.success("Alta compatibilidade")
    elif melhor[1] >= 50:
        st.info("Compatibilidade média")
    else:
        st.warning("Baixa compatibilidade")
