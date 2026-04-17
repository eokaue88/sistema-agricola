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
    # GRÃOS (principais do Brasil)
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "cultura": "soja"},
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "cultura": "milho"},
    {"solo": "argiloso", "clima": "umido", "regiao": "sul", "cultura": "arroz"},
    {"solo": "argiloso", "clima": "frio", "regiao": "sul", "cultura": "trigo"},
    {"solo": "argiloso", "clima": "ameno", "regiao": "sul", "cultura": "aveia"},
    {"solo": "misto", "clima": "quente", "regiao": "sudeste", "cultura": "feijao"},

    # CULTURAS COMERCIAIS
    {"solo": "argiloso", "clima": "quente", "regiao": "nordeste", "cultura": "cana"},
    {"solo": "argiloso", "clima": "ameno", "regiao": "sudeste", "cultura": "cafe"},
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "cultura": "algodao"},

    # FRUTAS (Brasil tropical)
    {"solo": "misto", "clima": "tropical", "regiao": "sudeste", "cultura": "laranja"},
    {"solo": "argiloso", "clima": "quente", "regiao": "norte", "cultura": "banana"},
    {"solo": "misto", "clima": "tropical", "regiao": "norte", "cultura": "manga"},
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "cultura": "abacaxi"},

    # CULTURAS SECAS (semiárido)
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "cultura": "mandioca"},
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "cultura": "sorgo"},
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "cultura": "milheto"},

    # HORTALIÇAS
    {"solo": "argiloso", "clima": "umido", "regiao": "sudeste", "cultura": "tomate"},
    {"solo": "misto", "clima": "ameno", "regiao": "sudeste", "cultura": "batata"},
    {"solo": "argiloso", "clima": "tropical", "regiao": "norte", "cultura": "pimenta"},

    # ROTAÇÃO (base científica)
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "cultura": "milho_safrinha"},
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "cultura": "soja_rotacao"}
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

    # ==============================
    # GRÁFICO
    # ==============================
    st.subheader("📈 Comparação")

    nomes = [c[0] for c in resultados]
    valores = [c[1] for c in resultados]

    st.bar_chart(valores)
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
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        ">
            <h3>{cultura.upper()}</h3>
            <p style="font-size: 20px;">{porc:.0f}% compatível</p>
            <p>#{i+1} recomendação</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(porc))

    # ==============================
    # RANKING (AGORA NO LUGAR CERTO)
    # ==============================
    st.subheader("🏆 Ranking de culturas")

    for i, (cultura, porc) in enumerate(resultados[:5], start=1):
        if i == 1:
            st.success(f"🥇 {cultura} — {porc:.0f}%")
        elif i == 2:
            st.info(f"🥈 {cultura} — {porc:.0f}%")
        elif i == 3:
            st.warning(f"🥉 {cultura} — {porc:.0f}%")
        else:
            st.write(f"{i}º lugar — {cultura} ({porc:.0f}%)")

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
