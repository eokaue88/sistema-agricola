import streamlit as st

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(
    page_title="AgroSmart",
    page_icon="🌱",
    layout="wide"
)

# ==============================
# ESTILO (CSS)
# ==============================
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #2e7d32;
}
.subtitle {
    color: gray;
    margin-bottom: 20px;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}
.metric {
    font-size: 25px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.markdown('<p class="main-title">🌱 AgroSmart</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Sistema inteligente de recomendação agrícola</p>', unsafe_allow_html=True)

# ==============================
# BASE DE DADOS
# ==============================
dados = [
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "cultura": "milho"},
    {"solo": "argiloso", "clima": "umido", "regiao": "sul", "cultura": "arroz"},
    {"solo": "misto", "clima": "quente", "regiao": "sudeste", "cultura": "feijao"},
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "cultura": "mandioca"},
    {"solo": "argiloso", "clima": "quente", "regiao": "nordeste", "cultura": "cana"},
    {"solo": "argiloso", "clima": "ameno", "regiao": "sudeste", "cultura": "cafe"},
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "cultura": "algodao"},
    {"solo": "arenoso", "clima": "frio", "regiao": "sul", "cultura": "trigo"},
    {"solo": "arenoso", "clima": "seco", "regiao": "centro-oeste", "cultura": "sorgo"},
    {"solo": "arenoso", "clima": "tropical", "regiao": "sudeste", "cultura": "amendoim"},
    {"solo": "argiloso", "clima": "umido", "regiao": "norte", "cultura": "cacau"}
]

# ==============================
# INPUTS
# ==============================
st.markdown("### 📥 Dados da propriedade")

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

    # ==============================
    # MÉTRICAS (DASHBOARD)
    # ==============================
    st.markdown("### 📊 Resultado da análise")

    m1, m2 = st.columns(2)

    with m1:
        st.metric("🌱 Melhor cultura", melhor[0])

    with m2:
        st.metric("📊 Compatibilidade", f"{melhor[1]:.0f}%")

    # ==============================
    # GRÁFICO
    # ==============================
    st.markdown("### 📈 Comparação das culturas")

    culturas = [c[0] for c in resultados]
    valores = [c[1] for c in resultados]

    st.bar_chart(valores)

    # ==============================
    # RANKING
    # ==============================
    st.markdown("### 🏆 Ranking")

    for i, (cultura, porc) in enumerate(resultados, start=1):
        if i == 1:
            st.success(f"🥇 {cultura} — {porc:.0f}%")
        elif i == 2:
            st.info(f"🥈 {cultura} — {porc:.0f}%")
        elif i == 3:
            st.warning(f"🥉 {cultura} — {porc:.0f}%")
        else:
            st.write(f"{i}º {cultura} — {porc:.0f}%")

    # ==============================
    # EXPLICAÇÃO AUTOMÁTICA
    # ==============================
    st.markdown("### 🧠 Análise do sistema")

    if melhor[1] == 100:
        st.success("Condições ideais para essa cultura. Alto potencial de produtividade.")
    elif melhor[1] >= 66:
        st.info("Boa compatibilidade. Pode gerar bons resultados com manejo adequado.")
    else:
        st.warning("Baixa compatibilidade. Recomendado revisar condições ou considerar outra cultura.")
