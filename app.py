import streamlit as st

# Base de dados
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

st.title("🌱 Sistema Agrícola Inteligente")

solo = st.selectbox("Escolha o solo", ["arenoso", "argiloso", "misto"])
clima = st.selectbox("Escolha o clima", ["quente", "umido", "seco", "frio", "ameno", "tropical"])
regiao = st.selectbox("Escolha a região", ["nordeste", "sul", "sudeste", "norte", "centro-oeste"])

if st.button("Recomendar"):
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

    st.success(f"🌱 Melhor cultura: {melhor[0]}")
    st.info(f"📊 Compatibilidade: {melhor[1]:.0f}%")

    st.subheader("📋 Ranking")
    for cultura, porc in resultados:
        st.write(f"{cultura} → {porc:.0f}%")
