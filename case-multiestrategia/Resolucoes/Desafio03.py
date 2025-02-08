import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="FII Dashboard", layout="wide")

@st.cache_data
def load_data():
    df_neg = pd.read_excel(
        r"C:\Users\luish\OneDrive\Área de Trabalho\Python Projetos\case-multiestrategia\dados\01_cleaned_data\negociacao_fiis.xlsx",
        parse_dates=["dt_pregao"]
    )
    df_div = pd.read_excel(
        r"C:\Users\luish\OneDrive\Área de Trabalho\Python Projetos\case-multiestrategia\dados\01_cleaned_data\dividendos_fiis.xlsx",
        parse_dates=["data_com"]
    )
    # Uniformiza o nome do ticker para facilitar o merge
    df_neg.rename(columns={"cod_negociacao_papel": "ticker"}, inplace=True)
    return df_neg.sort_values("dt_pregao"), df_div.sort_values("data_com")

df_neg, df_div = load_data()

# Seletor de ticker
tickers = sorted(df_neg["ticker"].unique())
selected_ticker = st.selectbox("Selecione o ticker", tickers)

# Filtra dados de negociação do ticker selecionado
df_ticker = df_neg[df_neg["ticker"] == selected_ticker]

# Gráfico 1: Preço de Fechamento e Volume Negociado
fig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1.add_trace(
    go.Scatter(
        x=df_ticker["dt_pregao"],
        y=df_ticker["preco_fechamento"],
        name="Preço Fechamento",
        mode="lines"
    ),
    secondary_y=False
)
fig1.add_trace(
    go.Bar(
        x=df_ticker["dt_pregao"],
        y=df_ticker["volume_negociado"],
        name="Volume Negociado"
    ),
    secondary_y=True
)
fig1.update_layout(
    title=f"{selected_ticker} - Preço e Volume",
    xaxis_title="Data",
    yaxis_title="Preço Fechamento"
)
fig1.update_yaxes(title_text="Volume Negociado", secondary_y=True)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Dividend Yield em %
df_div_ticker = df_div[df_div["ticker"] == selected_ticker].sort_values("data_com")
df_ticker_sorted = df_ticker.sort_values("dt_pregao")
df_merged = pd.merge_asof(
    df_ticker_sorted,
    df_div_ticker,
    left_on="dt_pregao",
    right_on="data_com",
    by="ticker",
    allow_exact_matches=False
)

# Calcula o Dividend Yield anualizado e converte para %
df_merged["dividend_yield_percent"] = (((1 + df_merged["dividendo"] / df_merged["preco_fechamento"]) ** 12) - 1) * 100

fig2 = go.Figure()
fig2.add_trace(
    go.Scatter(
        x=df_merged["dt_pregao"],
        y=df_merged["dividend_yield_percent"],
        mode="lines",
        name="Dividend Yield"
    )
)
fig2.update_layout(
    title=f"{selected_ticker} - Dividend Yield",
    xaxis_title="Data",
    yaxis_title="Dividend Yield (%)"
)
fig2.update_yaxes(ticksuffix="%", tickformat=".2f")
st.plotly_chart(fig2, use_container_width=True)
