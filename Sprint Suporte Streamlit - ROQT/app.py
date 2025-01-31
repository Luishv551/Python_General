import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ROQT - SUPORTE SPRINT",
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="collapsed"
)

# CSS para tema dark
st.markdown("""
    <style>
        .stApp {
            background-color: #0A0A0A;
            color: #FAFAFA;
        }
        
        h1, h4 {
            color: #FAFAFA !important;
            font-weight: 200 !important;
        }
        
        .stDataFrame {
            background-color: #1A1A1A;
        }
        
        div[data-testid="stDataFrameResizable"] {
            background-color: #1A1A1A !important;
        }
        
        .dataframe {
            background-color: #1A1A1A !important;
            border: none !important;
        }
        
        .dataframe th, .dataframe td {
            background-color: #1A1A1A !important;
            color: #FAFAFA !important;
            border: none !important;
            border-bottom: 1px solid #333 !important;
        }
        
        #MainMenu, footer {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("ROQT - SUPORTE SPRINT")

# DESENVOLVIMENTO - STATUS PROJETOS
st.header("DESENVOLVIMENTO - STATUS PROJETOS")
st.caption("Status atual dos projetos em desenvolvimento")
st.data_editor(
    pd.DataFrame(columns=["Cliente", "Responsável", "Situação"]),
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,
    key="dev_status"
)

# SUPORTE - TICKETS TRAVADOS
st.header("SUPORTE - TICKETS TRAVADOS")
st.caption("Tickets pendentes de resolução")
st.data_editor(
    pd.DataFrame(columns=["Cliente", "Responsável", "Situação"]),
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,
    key="tickets_travados"
)

# SUPORTE - STATUS EVOLUÇÕES
st.header("SUPORTE - STATUS EVOLUÇÕES")
st.caption("Evoluções e atualizações em andamento")
st.data_editor(
    pd.DataFrame(columns=["Cliente", "Responsável", "Situação"]),
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,
    key="evolucoes"
)

# DEMANDAS AVULSAS
st.header("DEMANDAS AVULSAS")
st.caption("Demandas diversas com priorização")
st.data_editor(
    pd.DataFrame(columns=["Tarefa", "Responsável", "Observação", "Prioridade"]),
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,
    column_config={
        "Prioridade": st.column_config.SelectboxColumn(
            options=["Baixa", "Média", "Alta"],
            required=True
        )
    },
    key="demandas"
)