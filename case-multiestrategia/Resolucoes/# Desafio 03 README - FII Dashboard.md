# Dashboard FIIs

**Acesse o dashboard aqui: [FII Dashboard App](https://dashboardfiis.streamlit.app/)**

## Sobre o Projeto
Este é um dashboard para análise de Fundos de Investimento Imobiliário (FIIs) que permite visualizar dados de negociação e dividend yield dos FIIs brasileiros.

## Estrutura
O projeto possui dois arquivos Excel principais:
- `negociacao_fiis.xlsx`: Contém dados de negociação dos FIIs
- `dividendos_fiis.xlsx`: Contém dados de dividendos dos FIIs

## Funcionalidades
- Visualização de preços e volumes de negociação
- Análise de dividend yield
- Seleção interativa de tickers
- Gráficos atualizados automaticamente

## Tecnologias Utilizadas
- Streamlit
- Pandas
- Plotly

## Instalação
Instale as dependências necessárias:
```bash
pip install streamlit pandas plotly requests openpyxl
```

## Como Executar
Execute o aplicativo com o comando:
```bash
streamlit run app.py
```