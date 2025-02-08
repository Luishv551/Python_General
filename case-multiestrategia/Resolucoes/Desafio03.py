import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
from io import BytesIO

st.set_page_config(page_title="FII Dashboard", layout="wide")

@st.cache_data
def load_data():
    # URLs dos arquivos raw no GitHub
    neg_url = "https://github.com/Luishv551/Python_General/raw/main/case-multiestrategia/dados/01_cleaned_data/negociacao_fiis.xlsx"
    div_url = "https://github.com/Luishv551/Python_General/raw/main/case-multiestrategia/dados/01_cleaned_data/dividendos_fiis.xlsx"
    
    # Função para baixar e ler os arquivos
    def download_excel(url):
        response = requests.get(url)
        return pd.read_excel(BytesIO(response.content))
    
    # Carrega os dados
    try:
        df_neg = download_excel(neg_url)
        df_div = download_excel(div_url)
        
        # Converte as colunas de data
        df_neg['dt_pregao'] = pd.to_datetime(df_neg['dt_pregao'])
        df_div['data_com'] = pd.to_datetime(df_div['data_com'])
        
        # Uniformiza o nome do ticker
        df_neg.rename(columns={"cod_negociacao_papel": "ticker"}, inplace=True)
        
        return df_neg.sort_values("dt_pregao"), df_div.sort_values("data_com")
    
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {str(e)}")
        return None, None

df_neg, df_div = load_data()

if df_neg is not None and df_div is not None:
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
else:
    st.error("Não foi possível carregar os dados. Por favor, verifique as URLs e tente novamente.")