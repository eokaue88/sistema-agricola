import streamlit as st

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="AgroSmart PRO",
    page_icon="🌱",
    layout="wide"
)

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("🌱 AgroSmart PRO")
st.sidebar.markdown("Sistema inteligente de recomendação agrícola")

st.sidebar.markdown("### ℹ️ Sobre")
st.sidebar.info("Este sistema analisa solo, clima e região para recomendar culturas com base em compatibilidade.")

# Histórico
if "historico" not in st.session_state:
    st.session_state.historico = []

# ==============================
# TÍTULO
# ==============================
st.title("🌱 AgroSmart PRO")
st.caption("Tecnologia aplicada ao agronegócio")

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
st.subheader("📥 Dados da propriedade")

col1, col2, col3 = st.columns(3)

with col1:
    solo = st.selectbox("🌍 Solo", ["arenoso", "argiloso", "misto"])

with col2:
    clima = st.selectbox("☁️ Clima", ["quente", "umido", "seco", "frio", "ameno", "tropical"])

with col3:
    regiao = st.selectbox("📍 Região", ["nordeste", "sul", "sudeste", "norte", "centro-oeste"])

# ==============================
# PROCESSAMENTO
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

    # Salvar no histórico
    st.session_state.historico.append({
        "solo": solo,
        "clima": clima,
        "regiao": regiao,
        "resultado": melhor[0]
    })

    # ==============================
    # DASHBOARD
    # ==============================
    st.subheader("📊 Resultado")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🌱 Cultura recomendada", melhor[0])

    with c2:
        st.metric("📊 Compatibilidade", f"{melhor[1]:.0f}%")

    with c3:
        nivel = "Alta" if melhor[1] >= 66 else "Baixa"
        st.metric("📈 Nível", nivel)

    # ==============================
    # GRÁFICO
    # ==============================
    st.subheader("📈 Comparação")

    nomes = [c[0] for c in resultados]
    valores = [c[1] for c in resultados]

    st.bar_chart(valores)

    # ==============================
    # EXPLICAÇÃO INTELIGENTE
    # ==============================
    st.subheader("🧠 Análise inteligente")

    if melhor[1] == 100:
        st.success("Condições perfeitas para essa cultura. Alto potencial produtivo.")
    elif melhor[1] >= 66:
        st.info("Boa compatibilidade. Com manejo adequado, pode gerar bons resultados.")
    else:
        st.warning("Baixa compatibilidade. Considere ajustar fatores ou escolher outra cultura.")

# ==============================
# HISTÓRICO
# ==============================
st.subheader("📜 Histórico de análises")

if st.session_state.historico:
    for item in reversed(st.session_state.historico[-5:]):
        st.write(f"{item['solo']} | {item['clima']} | {item['regiao']} → 🌱 {item['resultado']}")
else:
    st.write("Nenhuma análise realizada ainda.")
