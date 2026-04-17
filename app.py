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
# IMAGENS DAS CULTURAS
# ==============================
imagens = {
    "soja": "https://cdn.pixabay.com/photo/2016/03/05/19/02/soybean-1238252_1280.jpg",
    "milho": "https://cdn.pixabay.com/photo/2017/07/11/11/30/corn-2493131_1280.jpg",
    "arroz": "https://cdn.pixabay.com/photo/2016/11/29/09/08/rice-1867841_1280.jpg",
    "trigo": "https://cdn.pixabay.com/photo/2016/07/20/11/49/wheat-1529967_1280.jpg",
    "feijao": "https://cdn.pixabay.com/photo/2016/08/11/23/17/beans-1585499_1280.jpg",
    "cana": "https://cdn.pixabay.com/photo/2017/01/20/00/30/sugarcane-1995056_1280.jpg",
    "cafe": "https://cdn.pixabay.com/photo/2016/11/29/04/17/coffee-1869598_1280.jpg",
    "algodao": "https://cdn.pixabay.com/photo/2017/01/06/19/15/cotton-1959508_1280.jpg",
    "banana": "https://cdn.pixabay.com/photo/2018/06/03/14/00/banana-3453442_1280.jpg",
    "manga": "https://cdn.pixabay.com/photo/2017/01/20/15/06/mango-1995059_1280.jpg",
    "laranja": "https://cdn.pixabay.com/photo/2016/03/05/19/02/oranges-1238253_1280.jpg",
    "abacaxi": "https://cdn.pixabay.com/photo/2016/03/05/19/02/pineapple-1238254_1280.jpg",
    "mandioca": "https://cdn.pixabay.com/photo/2017/09/02/23/00/cassava-2706487_1280.jpg",
    "sorgo": "https://cdn.pixabay.com/photo/2016/11/18/13/47/grain-1837013_1280.jpg",
    "milheto": "https://cdn.pixabay.com/photo/2017/06/02/18/24/millet-2366348_1280.jpg",
    "tomate": "https://cdn.pixabay.com/photo/2016/03/05/19/02/tomatoes-1238255_1280.jpg",
    "batata": "https://cdn.pixabay.com/photo/2016/03/05/19/02/potatoes-1238256_1280.jpg",
    "pimenta": "https://cdn.pixabay.com/photo/2016/11/29/09/08/chili-1867842_1280.jpg"
}
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

# # ==============================
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

    valores = [c[1] for c in resultados]
    st.bar_chart(valores)

    ## ==============================
# CARDS COM IMAGEM (ESTILO NETFLIX)
# ==============================
st.markdown("## 🍿 Recomendações para você")

cols = st.columns(3)

for i, (cultura, porc) in enumerate(resultados[:6]):
    with cols[i % 3]:
        cor = "#2e7d32" if i == 0 else "#1e1e1e"

        imagem = imagens.get(cultura, "https://via.placeholder.com/300")

        st.markdown(f"""
        <div style="
            background-color: {cor};
            padding: 10px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        ">
            <img src="{imagem}" style="width:100%; border-radius:10px;">
            <h3>{cultura.upper()}</h3>
            <p style="font-size: 18px;">{porc:.0f}% compatível</p>
            <p>#{i+1} recomendação</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(porc))
    # ==============================
    # RANKING
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
