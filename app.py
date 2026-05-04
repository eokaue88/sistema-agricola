import streamlit as st
import base64
import streamlit.components.v1 as components
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

st.set_page_config(
    page_title="AgroSmart PRO",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Oxanium:wght@300;400;600&display=swap');

.stApp {
    background: radial-gradient(circle at top, #23306b 0%, #171B48 45%, #090b1f 100%);
}

.block-container {
    max-width: 1100px;
    margin: auto;
    padding-top: 2rem;
}

.stApp, .stApp p, .stApp label, .stApp div, .stApp h1, .stApp h2, .stApp h3,
.stApp h4, .stApp h5, .stApp h6, .stButton button, .stSelectbox *, .stTextInput * {
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

.stSelectbox>div>div,
.stTextInput>div>div>input {
    background: rgba(255,255,255,0.08);
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.2);
    color: white;
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
    animation: fadeIn 0.6s ease-in-out;
}

.card-agro:hover {
    transform: translateY(-8px) scale(1.04);
    box-shadow: 0 20px 50px rgba(17,161,126,0.5);
}

.card-top1 {
    background: linear-gradient(160deg, #11A17E, #064c3e);
    border: 2px solid rgba(255,255,255,0.5);
    transform: scale(1.02);
    animation: fadeIn 0.8s ease-in-out;
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

.top-card {
    background: linear-gradient(160deg, rgba(255,255,255,0.13), rgba(255,255,255,0.05));
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 18px;
    padding: 18px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.35);
    min-height: 130px;
}

.top-card h3 {
    margin: 8px 0;
    font-size: 22px;
}

.top-card h2 {
    margin: 8px 0;
    font-size: 30px;
}

.info-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 18px;
    padding: 18px;
    color: white;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}

[data-testid="stVerticalBlock"] {
    gap: 1.2rem;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

def carregar_logo(path):
    try:
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()
    except FileNotFoundError:
        return None

logo_base64 = carregar_logo("logo.png")

logo_html = ""
if logo_base64:
    logo_html = f'<img class="logo-agro" src="data:image/png;base64,{logo_base64}">'

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
    {logo_html}
    <div class="titulo-agro">AgroSmart PRO</div>
    <div class="subtitulo-agro">Tecnologia aplicada ao agronegócio</div>
</div>
""", height=190)
st.caption("Versão 1.0")

st.sidebar.markdown("## 🌱 AgroSmart PRO")
st.sidebar.info("Sistema inteligente de recomendação agrícola")
pagina = st.sidebar.radio(
    "📌 Navegação",
    ["🌾 Recomendação agrícola", "⛰️ Serra da Ibiapaba - CE"]
)

if "historico" not in st.session_state:
    st.session_state.historico = []

if "resultados" not in st.session_state:
    st.session_state.resultados = []

if "mostrar_tabela" not in st.session_state:
    st.session_state.mostrar_tabela = False

if st.sidebar.button("🗑️ Limpar histórico"):
    st.session_state.historico = []

dados = [
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "objetivo": "grãos", "cultura": "soja"},
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "objetivo": "grãos", "cultura": "milho"},
    {"solo": "argiloso", "clima": "umido", "regiao": "sul", "objetivo": "grãos", "cultura": "arroz"},
    {"solo": "argiloso", "clima": "frio", "regiao": "sul", "objetivo": "grãos", "cultura": "trigo"},
    {"solo": "misto", "clima": "quente", "regiao": "sudeste", "objetivo": "grãos", "cultura": "feijao"},

    {"solo": "argiloso", "clima": "ameno", "regiao": "sudeste", "objetivo": "comercial", "cultura": "cafe"},
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "objetivo": "comercial", "cultura": "algodao"},
    {"solo": "argiloso", "clima": "quente", "regiao": "nordeste", "objetivo": "comercial", "cultura": "cana-de-açúcar"},

    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "objetivo": "alimentação", "cultura": "mandioca"},
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "objetivo": "alimentação", "cultura": "sorgo"},
    {"solo": "arenoso", "clima": "seco", "regiao": "nordeste", "objetivo": "alimentação", "cultura": "milheto"},

    {"solo": "misto", "clima": "tropical", "regiao": "sudeste", "objetivo": "fruticultura", "cultura": "laranja"},
    {"solo": "argiloso", "clima": "quente", "regiao": "norte", "objetivo": "fruticultura", "cultura": "banana"},
    {"solo": "misto", "clima": "tropical", "regiao": "norte", "objetivo": "fruticultura", "cultura": "manga"},
    {"solo": "arenoso", "clima": "quente", "regiao": "nordeste", "objetivo": "fruticultura", "cultura": "abacaxi"},

    {"solo": "argiloso", "clima": "umido", "regiao": "sudeste", "objetivo": "hortaliças", "cultura": "tomate"},
    {"solo": "misto", "clima": "ameno", "regiao": "sudeste", "objetivo": "hortaliças", "cultura": "batata"},
    {"solo": "argiloso", "clima": "tropical", "regiao": "norte", "objetivo": "hortaliças", "cultura": "pimenta"},

    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "objetivo": "rotação", "cultura": "milho safrinha"},
    {"solo": "argiloso", "clima": "quente", "regiao": "centro-oeste", "objetivo": "rotação", "cultura": "soja em rotação"},
]

icones = {
    "soja": "🌱",
    "milho": "🌽",
    "arroz": "🍚",
    "trigo": "🌾",
    "feijao": "🫘",
    "cafe": "☕",
    "algodao": "🧵",
    "mandioca": "🥔",
    "tomate": "🍅",
    "cana-de-açúcar": "🎋",
    "sorgo": "🌾",
    "milheto": "🌾",
    "laranja": "🍊",
    "banana": "🍌",
    "manga": "🥭",
    "abacaxi": "🍍",
    "batata": "🥔",
    "pimenta": "🌶️",
    "milho safrinha": "🌽",
    "soja em rotação": "🌱"
}
links_culturas = {
    "soja": "https://www.youtube.com/results?search_query=como+plantar+soja",
    "milho": "https://www.youtube.com/results?search_query=como+plantar+milho",
    "arroz": "https://www.youtube.com/results?search_query=como+plantar+arroz",
    "trigo": "https://www.youtube.com/results?search_query=como+plantar+trigo",
    "feijao": "https://www.youtube.com/results?search_query=como+plantar+feijao",
    "cafe": "https://www.youtube.com/results?search_query=como+plantar+cafe",
    "mandioca": "https://www.youtube.com/results?search_query=como+plantar+mandioca",
    "tomate": "https://www.youtube.com/results?search_query=como+plantar+tomate",
    "banana": "https://www.youtube.com/results?search_query=como+plantar+banana",
    "manga": "https://www.youtube.com/results?search_query=como+plantar+manga",
    "laranja": "https://www.youtube.com/results?search_query=como+plantar+laranja",
    "algodao": "https://www.youtube.com/results?search_query=como+plantar+algodao"
    
}
observacoes = {
    "soja": "Indicada para regiões quentes e solos férteis, sendo muito comum no Centro-Oeste brasileiro.",
    "milho": "Adapta-se bem a clima quente e pode ser usado tanto para grãos quanto para rotação de culturas.",
    "arroz": "Tem melhor desempenho em ambientes úmidos e solos argilosos.",
    "trigo": "É mais indicado para regiões de clima frio, especialmente no Sul do Brasil.",
    "feijao": "Pode se adaptar bem a solos mistos e clima quente, dependendo do manejo.",
    "cafe": "Prefere clima ameno e solos bem estruturados, comum no Sudeste.",
    "algodao": "Cultura comercial importante em regiões quentes, exigindo bom controle de pragas.",
    "mandioca": "É resistente à seca e indicada para solos arenosos, sendo forte no semiárido nordestino.",
    "tomate": "Exige boa disponibilidade de água, manejo cuidadoso e solos bem preparados.",
    "cana-de-açúcar": "É uma cultura comercial forte em regiões quentes e solos bem manejados.",
    "sorgo": "Tem boa resistência à seca e pode ser usado na alimentação animal e humana.",
    "milheto": "É resistente ao clima seco e pode ajudar na cobertura do solo.",
    "laranja": "É uma fruta de valor comercial, comum em regiões tropicais e subtropicais.",
    "banana": "Adapta-se bem a clima quente e úmido, comum no Norte e Nordeste.",
    "manga": "É uma fruta tropical resistente ao calor e muito cultivada em regiões quentes.",
    "abacaxi": "Adapta-se bem a solos arenosos e clima quente.",
    "batata": "Prefere clima ameno e solos bem preparados.",
    "pimenta": "Cultura de bom valor comercial, adaptada a ambientes tropicais.",
    "milho safrinha": "Boa opção para rotação após a soja em regiões agrícolas consolidadas.",
    "soja em rotação": "Pode contribuir para planejamento agrícola em áreas de grãos."
}

pontos_positivos = {
    "soja": "Alta demanda comercial e boa adaptação ao Centro-Oeste.",
    "milho": "Versátil, usado para alimentação, ração e rotação.",
    "arroz": "Boa produtividade em ambientes úmidos.",
    "trigo": "Importante para regiões frias e para produção de farinha.",
    "feijao": "Alimento básico e de grande importância no Brasil.",
    "cafe": "Produto de alto valor comercial.",
    "algodao": "Boa rentabilidade em sistemas comerciais.",
    "mandioca": "Alta resistência à seca e fácil adaptação.",
    "tomate": "Alto valor de mercado.",
    "cana-de-açúcar": "Boa produtividade e uso industrial.",
    "sorgo": "Resistente à seca.",
    "milheto": "Ajuda na proteção e cobertura do solo.",
    "laranja": "Boa aceitação no mercado de frutas.",
    "banana": "Produção contínua e boa demanda.",
    "manga": "Boa valorização em regiões tropicais.",
    "abacaxi": "Boa adaptação ao calor.",
    "batata": "Alimento de grande consumo.",
    "pimenta": "Pode gerar boa rentabilidade em pequenas áreas.",
    "milho safrinha": "Aproveita melhor o calendário agrícola.",
    "soja em rotação": "Ajuda no planejamento produtivo da propriedade."
}

cuidados = {
    "soja": "Exige manejo adequado do solo e controle de pragas.",
    "milho": "Precisa de boa disponibilidade de nutrientes.",
    "arroz": "Pode exigir bastante água.",
    "trigo": "Sensível a temperaturas muito altas.",
    "feijao": "Exige atenção com doenças e irrigação.",
    "cafe": "Demanda manejo cuidadoso e tempo até boa produção.",
    "algodao": "Exige controle rigoroso de pragas.",
    "mandioca": "Pode ter ciclo mais longo de produção.",
    "tomate": "Muito sensível a pragas e doenças.",
    "cana-de-açúcar": "Exige planejamento de área e colheita.",
    "sorgo": "Pode ter menor valor comercial em algumas regiões.",
    "milheto": "Geralmente precisa ser bem planejado no sistema produtivo.",
    "laranja": "Exige controle de doenças e pragas.",
    "banana": "Precisa de boa disponibilidade de água.",
    "manga": "Exige poda e manejo correto.",
    "abacaxi": "Pode exigir controle de plantas daninhas.",
    "batata": "Sensível a doenças de solo.",
    "pimenta": "Precisa de manejo cuidadoso e irrigação.",
    "milho safrinha": "Depende muito da janela de plantio.",
    "soja em rotação": "Deve ser planejada para evitar desgaste do solo."
}

pesos = {
    "solo": 2,
    "clima": 3,
    "regiao": 1,
    "objetivo": 2
}

def classificar_recomendacao(porc):
    if porc >= 80:
        return "Alta recomendação"
    elif porc >= 50:
        return "Recomendação média"
    else:
        return "Baixa recomendação"


def gerar_pdf_relatorio(nome_prop, solo, clima, regiao, objetivo, cultura, compatibilidade, nivel, observacao, ponto_positivo, cuidado):
    from datetime import datetime
    import random

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "TituloAgro",
        parent=styles["Title"],
        fontSize=26,
        textColor=colors.HexColor("#11A17E"),
        alignment=1,
        spaceAfter=6
    )

    subtitulo = ParagraphStyle(
        "SubtituloAgro",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.HexColor("#064c3e"),
        spaceAfter=10
    )

    texto = ParagraphStyle(
        "TextoAgro",
        parent=styles["BodyText"],
        fontSize=10.5,
        leading=15,
        spaceAfter=8
    )

    aviso = ParagraphStyle(
        "AvisoAgro",
        parent=styles["BodyText"],
        fontSize=9,
        textColor=colors.HexColor("#555555"),
        leading=13,
        spaceBefore=12
    )

    elementos = []

    # 🔥 TÍTULO COM BRANDING
    elementos.append(Paragraph(
        "AgroSmart PRO • Sistema Inteligente de Recomendação Agrícola",
        titulo
    ))

    # 📅 DATA + CÓDIGO
    data_atual = datetime.now().strftime('%d/%m/%Y')
    codigo = f"AGRO-{random.randint(1000,9999)}"

    elementos.append(Paragraph(f"Data da análise: {data_atual}", texto))
    elementos.append(Paragraph(f"Código do relatório: {codigo}", texto))

    elementos.append(Spacer(1, 12))

    # 📊 RESUMO PRINCIPAL
    resumo = Table([
        ["Melhor cultura", cultura.upper()],
        ["Compatibilidade", f"{compatibilidade:.0f}%"],
        ["Nível", nivel],
    ], colWidths=[150, 320])

    resumo.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#064c3e")),
        ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#11A17E")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.white),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("PADDING", (0, 0), (-1, -1), 10),
    ]))

    elementos.append(resumo)
    elementos.append(Spacer(1, 18))

    # 📥 DADOS DA ANÁLISE
    dados_tabela = [
        ["Propriedade", nome_prop if nome_prop else "Não informado"],
        ["Solo", solo],
        ["Clima", clima],
        ["Região", regiao],
        ["Objetivo", objetivo],
    ]

    tabela = Table(dados_tabela, colWidths=[140, 330])
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#11A17E")),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
        ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#F4F7F5")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elementos.append(Paragraph("Dados da análise", subtitulo))
    elementos.append(tabela)
    elementos.append(Spacer(1, 16))

    # 🧠 CONTEÚDO
    elementos.append(Paragraph("Observação técnica", subtitulo))
    elementos.append(Paragraph(observacao, texto))

    elementos.append(Paragraph("Ponto positivo", subtitulo))
    elementos.append(Paragraph(ponto_positivo, texto))

    elementos.append(Paragraph("Cuidados recomendados", subtitulo))
    elementos.append(Paragraph(cuidado, texto))

    elementos.append(Spacer(1, 12))

    elementos.append(Paragraph(
        "Análise baseada em padrões agrícolas brasileiros e dados simulados com base em condições ideais de cultivo.",
        texto
    ))

    elementos.append(Paragraph(
        "Aviso: este sistema possui finalidade educativa e não substitui uma análise agronômica profissional.",
        aviso
    ))

    doc.build(elementos)
    buffer.seek(0)
    return buffer
if pagina == "⛰️ Serra da Ibiapaba - CE":
    st.markdown("## ⛰️ Serra da Ibiapaba - Ceará")
    st.info("Área dedicada às características agrícolas e regionais da Serra da Ibiapaba.")

    st.markdown("""
    A Serra da Ibiapaba é uma região importante do Ceará, conhecida pelo clima mais ameno,
    relevo serrano e potencial para agricultura, fruticultura, hortaliças e produção familiar.
    """)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.metric("🌡️ Clima", "Mais ameno")

    with col_b:
        st.metric("🌱 Potencial", "Fruticultura")

    with col_c:
        st.metric("📍 Região", "Ceará")

    st.markdown("### 🌾 Culturas com bom potencial na região")

    st.markdown("""
    - Banana  
    - Café  
    - Hortaliças  
    - Tomate  
    - Pimenta  
    - Frutas tropicais  
    """)

    st.markdown("### 💡 Observação")
    st.warning("Essas informações são educativas e podem variar conforme solo, altitude, manejo e disponibilidade de água.")

    st.stop()    
st.subheader("📥 Dados da propriedade")

nome_prop = st.text_input("🏡 Nome da propriedade")

col_est1, col_est2, col_est3 = st.columns(3)

with col_est1:
    st.metric("🌾 Culturas no banco", len(dados))

with col_est2:
    st.metric("⚙️ Critérios analisados", len(pesos))

with col_est3:
    st.metric("📜 Histórico", len(st.session_state.historico))

st.info("Informe os dados da propriedade e clique em gerar recomendação para receber a melhor cultura indicada pelo sistema.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    solo = st.selectbox("🌍 Solo", ["arenoso", "argiloso", "misto"])

with col2:
    clima = st.selectbox("☁️ Clima", ["quente", "umido", "seco", "frio", "ameno", "tropical"])

with col3:
    regiao = st.selectbox("📍 Região", ["nordeste", "sul", "sudeste", "norte", "centro-oeste"])

with col4:
    objetivo = st.selectbox("🎯 Objetivo", ["grãos", "alimentação", "comercial", "fruticultura", "hortaliças", "rotação"])

st.caption("⚠️ Este sistema possui finalidade educativa e não substitui uma análise agronômica profissional.")

if st.button("🚀 Gerar recomendação", use_container_width=True):

    # 🔄 Loading
    with st.spinner("Analisando dados da propriedade... 🌱"):
        import time
        time.sleep(1.2)

    st.success("✅ Análise concluída com sucesso!")

    resultados = []

    for item in dados:
        pontuacao = 0

        if item["solo"] == solo:
            pontuacao += pesos["solo"]
        elif solo == "misto" or item["solo"] == "misto":
            pontuacao += pesos["solo"] * 0.5

        if item["clima"] == clima:
            pontuacao += pesos["clima"]
        elif (clima == "tropical" and item["clima"] == "quente") or (clima == "quente" and item["clima"] == "tropical"):
            pontuacao += pesos["clima"] * 0.6
        elif (clima == "ameno" and item["clima"] in ["frio", "umido"]) or (item["clima"] == "ameno" and clima in ["frio", "umido"]):
            pontuacao += pesos["clima"] * 0.4

        if item["regiao"] == regiao:
            pontuacao += pesos["regiao"]

        if item["objetivo"] == objetivo:
            pontuacao += pesos["objetivo"]

        porcentagem = (pontuacao / sum(pesos.values())) * 100
        resultados.append((item["cultura"], porcentagem, item["objetivo"]))

    resultados.sort(key=lambda x: x[1], reverse=True)
    st.session_state.resultados = resultados

    melhor = resultados[0]
    cultura_melhor = melhor[0]
    icone_melhor = icones.get(cultura_melhor, "🌱")
    nivel = classificar_recomendacao(melhor[1])

    st.session_state.historico.append({
        "propriedade": nome_prop if nome_prop else "Não informado",
        "solo": solo,
        "clima": clima,
        "regiao": regiao,
        "objetivo": objetivo,
        "resultado": cultura_melhor,
        "compatibilidade": melhor[1],
        "nivel": nivel
    })

       # 🎯 CARD PRINCIPAL
    link = links_culturas.get(cultura_melhor)

    st.markdown(f"""
    <div class="card-agro card-top1" style="animation: fadeIn 0.8s ease;">
        <p>🎯 Melhor escolha para sua fazenda</p>
        <h3>{icone_melhor} {cultura_melhor.upper()}</h3>
        <p>{nivel}</p>
        <h2>{melhor[1]:.0f}%</h2>
    </div>
    """, unsafe_allow_html=True)
    if melhor[1] >= 80:
        st.success("🌟 Excelente escolha! Alta compatibilidade com sua propriedade.")
    elif melhor[1] >= 50:
        st.info("👍 Boa opção, mas pode exigir ajustes no manejo.")
    else:
        st.warning("⚠️ Baixa compatibilidade. Considere revisar os dados informados.")

     # 🔗 BOTÃO FUNCIONAL
    if link:
        st.link_button(
            f"▶️ Aprender a cultivar {cultura_melhor.capitalize()}",
            link,
            use_container_width=True
        )
    else:
        st.warning("⚠️ Conteúdo ainda não disponível para essa cultura.")
    st.caption("Conteúdo educativo externo com técnicas de plantio e manejo.")
    st.markdown("## 🥇 Top 3 recomendações")

    top_cols = st.columns(3)

    for i, (cultura, porc, _) in enumerate(resultados[:3]):
        with top_cols[i]:
            icone_top = icones.get(cultura, "🌱")
            st.markdown(f"""
            <div class="top-card">
                <p>#{i+1} colocação</p>
                <h3>{icone_top} {cultura.upper()}</h3>
                <h2>{porc:.0f}%</h2>
            </div>
            """, unsafe_allow_html=True)

    if melhor[1] < 50:
        st.error("⚠️ Baixa compatibilidade detectada. Considere revisar clima, solo ou objetivo.")
    
    st.divider()

    st.markdown("## 📄 Relatório da análise")

    relatorio = f"""
RELATÓRIO AGROSMART PRO

Nome da propriedade: {nome_prop if nome_prop else "Não informado"}
Solo informado: {solo}
Clima informado: {clima}
Região informada: {regiao}
Objetivo informado: {objetivo}

Melhor cultura: {cultura_melhor.upper()}
Compatibilidade: {melhor[1]:.0f}%
Nível: {nivel}

Explicação do cálculo:
O sistema compara os dados informados pelo usuário com o banco de culturas.
Pesos utilizados:
- Solo: {pesos["solo"]}
- Clima: {pesos["clima"]}
- Região: {pesos["regiao"]}
- Objetivo: {pesos["objetivo"]}

Pontuação máxima possível: {sum(pesos.values())} pontos.

Observação técnica:
{observacoes.get(cultura_melhor, "Essa cultura pode exigir análise mais detalhada.")}

Ponto positivo:
{pontos_positivos.get(cultura_melhor, "Pode apresentar bom potencial produtivo.")}

Cuidados:
{cuidados.get(cultura_melhor, "É importante consultar orientação técnica antes do plantio.")}

Aviso:
Este sistema possui finalidade educativa e não substitui uma análise agronômica profissional.
"""

    st.markdown(f"""
    <div class="info-box">
        <p><strong>Nome da propriedade:</strong> {nome_prop if nome_prop else "Não informado"}</p>
        <p><strong>Solo informado:</strong> {solo}</p>
        <p><strong>Clima informado:</strong> {clima}</p>
        <p><strong>Região informada:</strong> {regiao}</p>
        <p><strong>Objetivo:</strong> {objetivo}</p>
        <p><strong>Melhor cultura:</strong> {icone_melhor} {cultura_melhor.upper()}</p>
        <p><strong>Compatibilidade:</strong> {melhor[1]:.0f}%</p>
        <p><strong>Nível:</strong> {nivel}</p>
        <p>📍 Análise baseada em padrões agrícolas brasileiros.</p>
        <p>📊 Dados simulados com base em condições ideais de cultivo.</p>
    </div>
    """, unsafe_allow_html=True)

    pdf_relatorio = gerar_pdf_relatorio(
        nome_prop,
        solo,
        clima,
        regiao,
        objetivo,
        cultura_melhor,
        melhor[1],
        nivel,
        observacoes.get(cultura_melhor, "Essa cultura pode exigir análise mais detalhada."),
        pontos_positivos.get(cultura_melhor, "Pode apresentar bom potencial produtivo."),
        cuidados.get(cultura_melhor, "É importante consultar orientação técnica antes do plantio.")
    )

    col_pdf, col_txt = st.columns(2)

    with col_pdf:
        st.download_button(
            label="📄 Baixar relatório em PDF",
            data=pdf_relatorio,
            file_name="relatorio_agrosmart.pdf",
            mime="application/pdf"
        )

    with col_txt:
        st.download_button(
            label="📥 Baixar relatório em TXT",
            data=relatorio,
            file_name="relatorio_agrosmart.txt",
            mime="text/plain"
        )

    st.divider()

    st.markdown("### 🧠 Por que essa recomendação?")

    st.info(f"""
    A cultura **{cultura_melhor.upper()}** teve a maior compatibilidade com os dados informados.

    Pesos usados no cálculo:
    - Solo: {pesos["solo"]}
    - Clima: {pesos["clima"]}
    - Região: {pesos["regiao"]}
    - Objetivo: {pesos["objetivo"]}

    Observação técnica: {observacoes.get(cultura_melhor, "Essa cultura pode exigir uma análise mais detalhada.")}
    """)

    with st.expander("📘 Ver metodologia do sistema"):
        st.info(f"""
        O sistema compara os dados informados com o banco de culturas.

        Cada critério possui um peso:
        - Solo: {pesos["solo"]} pontos
        - Clima: {pesos["clima"]} pontos
        - Região: {pesos["regiao"]} ponto
        - Objetivo: {pesos["objetivo"]} pontos

        A pontuação final é convertida em porcentagem de compatibilidade.

        Fórmula usada:
        compatibilidade = (pontuação obtida / pontuação máxima) × 100
        """)

    st.markdown("### ✅ Pontos positivos e cuidados")

    col_pos, col_cuidado = st.columns(2)

    with col_pos:
        st.success(pontos_positivos.get(cultura_melhor, "Pode apresentar bom potencial produtivo."))

    with col_cuidado:
        st.warning(cuidados.get(cultura_melhor, "É importante consultar orientação técnica antes do plantio."))

    st.divider()

    st.markdown("## 🌾 Ranking de culturas recomendadas")

    qtd_colunas = 3
    cols = st.columns(qtd_colunas)

    for i, (cultura, porc, obj) in enumerate(resultados[:6]):
        with cols[i % qtd_colunas]:
            icone = icones.get(cultura, "🌱")
            nivel_card = classificar_recomendacao(porc)

            if nivel_card == "Alta recomendação":
                cor_card = "linear-gradient(160deg, #11A17E, #064c3e)"
            elif nivel_card == "Recomendação média":
                cor_card = "linear-gradient(160deg, #c9a227, #6b5410)"
            else:
                cor_card = "linear-gradient(160deg, #b23a48, #5c1119)"

            st.markdown(f"""
            <div class="card-agro" style="background: {cor_card};">
                <p>🥇 #{i+1}</p>
                <h3>{icone} {cultura.upper()}</h3>
                <p>{nivel_card}</p>
                <h2>{porc:.0f}%</h2>
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(porc))

if st.session_state.resultados:
    mostrar_tabela = st.toggle("📋 Ver tabela completa", value=False)

    if mostrar_tabela:
        tabela = pd.DataFrame(
            st.session_state.resultados,
            columns=["Cultura", "Compatibilidade", "Objetivo"]
        )
        tabela["Compatibilidade"] = tabela["Compatibilidade"].map(lambda x: f"{x:.0f}%")
        tabela["Nível"] = [
            classificar_recomendacao(porc)
            for _, porc, _ in st.session_state.resultados
        ]

        st.dataframe(tabela, use_container_width=True)

if st.session_state.historico:
    st.divider()
    st.markdown("## 📜 Histórico de análises")

    for h in st.session_state.historico[-5:][::-1]:
        st.write(
            f"🏡 **{h['propriedade']}** | 🌍 **{h['solo']}** | ☁️ **{h['clima']}** | "
            f"📍 **{h['regiao']}** | 🎯 **{h['objetivo']}** → "
            f"🌱 **{h['resultado'].upper()}** ({h['compatibilidade']:.0f}%) - **{h['nivel']}**"
        )

    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
    """, unsafe_allow_html=True)

    if st.button("🔄 Nova análise"):
        st.session_state.resultados = []
        st.session_state.mostrar_tabela = False
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
