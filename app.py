import streamlit as st
import base64
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
    page_title="AgroSmart PRO",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# ESTATÍSTICAS
# ==============================
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.metric("🌾 Culturas no banco", 20)

with col_b:
    st.metric("⚙️ Critérios analisados", 4)

with col_c:
    st.metric("📜 Histórico", len(st.session_state.get("historico", [])))

# ==============================
# INPUT EXTRA
# ==============================
nome_prop = st.text_input("🏡 Nome da propriedade")

# ==============================
# RESTANTE DO SEU CÓDIGO (INALTERADO)
# ==============================

# (mantive tudo igual até o botão...)

# ==============================
# BOTÃO
# ==============================
if st.button("🚀 Gerar recomendação"):

    resultados = []

    for item in dados:
        pontuacao = 0

        if item["solo"] == solo:
            pontuacao += pesos["solo"]
        if item["clima"] == clima:
            pontuacao += pesos["clima"]
        if item["regiao"] == regiao:
            pontuacao += pesos["regiao"]
        if item["objetivo"] == objetivo:
            pontuacao += pesos["objetivo"]

        porcentagem = (pontuacao / sum(pesos.values())) * 100
        resultados.append((item["cultura"], porcentagem, item["objetivo"]))

    resultados.sort(key=lambda x: x[1], reverse=True)
    melhor = resultados[0]
    cultura_melhor = melhor[0]
    icone_melhor = icones.get(cultura_melhor, "🌱")
    nivel = classificar_recomendacao(melhor[1])

    # ==============================
    # RELATÓRIO COM NOME
    # ==============================
    relatorio = f"""
RELATÓRIO AGROSMART PRO

Propriedade: {nome_prop}

Solo: {solo}
Clima: {clima}
Região: {regiao}
Objetivo: {objetivo}

Melhor cultura: {cultura_melhor}
Compatibilidade: {melhor[1]:.0f}%
Nível: {nivel}
"""

    st.download_button(
        label="📥 Baixar relatório",
        data=relatorio,
        file_name="relatorio.txt"
    )

    # ==============================
    # TABELA COMPLETA
    # ==============================
    if st.checkbox("📋 Ver tabela completa"):
        df = pd.DataFrame(resultados, columns=["Cultura", "Compatibilidade", "Objetivo"])
        df["Nível"] = df["Compatibilidade"].apply(classificar_recomendacao)
        st.dataframe(df)

    # ==============================
    # METODOLOGIA
    # ==============================
    if st.button("📘 Ver metodologia"):
        st.info("""
O sistema compara os dados informados com o banco de culturas.

Pesos utilizados:
- Solo: 2
- Clima: 3
- Região: 1
- Objetivo: 2
""")
