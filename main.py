import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Configuração da Página 
st.set_page_config(
    page_title="SAD - Arquitetura de Dashboards",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título e Descrição
st.title("Arquitetura de Dashboards de Dados")
st.markdown("### Uma Abordagem para o Aumento da Eficiência em Sistemas de Apoio à Tomada de Decisão")

# 2. Geração de Dados Sintéticos (Simulando fontes heterogêneas)
@st.cache_data
def load_data():
    dates = pd.date_range(start="2026-01-01", end="2026-04-20")
    data = pd.DataFrame({
        "Data": np.random.choice(dates, 100),
        "Setor": np.random.choice(["Financeiro", "Operacional", "Vendas", "Logística"], 100),
        "Eficiência": np.random.uniform(70, 98, 100),
        "Volume_Dados": np.random.randint(100, 1000, 100)
    })
    return data

df = load_data()

# 3. Barra Lateral (Elicitação de Requisitos de Filtro)
st.sidebar.header("Painel de Controle")
setor_selecionado = st.sidebar.multiselect(
    "Selecione o Setor para Análise:",
    options=df["Setor"].unique(),
    default=df["Setor"].unique()
)

# Filtragem dos dados
df_filtered = df[df["Setor"].isin(setor_selecionado)]

# 4. Indicadores de Eficiência (Métricas de Suporte à Decisão)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Eficiência Média", f"{df_filtered['Eficiência'].mean():.2f}%", delta="1.5%")
with col2:
    st.metric("Volume Processado", f"{df_filtered['Volume_Dados'].sum()} GB")
with col3:
    st.metric("Setores Ativos", len(setor_selecionado))

st.divider()

# 5. Visualizações Interativas
c1, c2 = st.columns(2)

with c1:
    st.subheader("Tendência de Eficiência por Setor")
    fig_line = px.line(df_filtered.sort_values("Data"), x="Data", y="Eficiência", color="Setor",
                       title="Variação Temporal da Eficiência")
    st.plotly_chart(fig_line, use_container_width=True)

with c2:
    st.subheader("Distribuição do Volume de Dados")
    fig_bar = px.bar(df_filtered, x="Setor", y="Volume_Dados", color="Setor",
                     title="Carga de Dados por Departamento")
    st.plotly_chart(fig_bar, use_container_width=True)

# 6. Tabela de Detalhes (Rastreabilidade da Decisão)
with st.expander("Visualizar Dados Brutos (ETL)"):
    st.dataframe(df_filtered, use_container_width=True)

# Rodapé Acadêmico
st.sidebar.markdown("---")
st.sidebar.info(f"Autor: José Vítor T. de Bortoli\n\nOrientador: Prof. Fabrício Herpich\n\nUFFS - Campus Chapecó")