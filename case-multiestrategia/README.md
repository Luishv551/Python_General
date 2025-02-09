# Projeto de Análise de FIIs - Multi Estratégia

## Visão Geral
Este projeto consiste em três desafios interligados focados na análise e visualização de dados de Fundos de Investimento Imobiliário (FIIs) brasileiros.

## Estrutura do Projeto
```
case-multiestrategia/
├── dados/
│   ├── 00_raw_data/
│   └── 01_cleaned_data/
├── Resolucoes/
│   ├── Desafio01.ipynb
│   ├── Desafio02.ipynb
│   ├── Desafio03.py
│   └── READMEs individuais
└── README.md
```

## Desafios

### [Desafio 01 - Consolidação IFIX](Resolucoes/%23%20Desafio%2001%20README%20-%20Consolidação%20IFIX.md)
- Consolidação de dados do índice IFIX
- Processamento de múltiplos arquivos CSV
- Validação e geração de logs

### [Desafio 02 - Análise de Negociação](Resolucoes/%23%20Desafio%2002%20README%20-%20Analise%20de%20Negociacao%20de%20FIIs.md)
- Análise de volumes de negociação
- Identificação de máximos históricos
- Cálculos de métricas do IFIX

### [Desafio 03 - Dashboard FIIs](Resolucoes/%23%20Desafio%2003%20README%20-%20FII%20Dashboard.md)
- Dashboard interativo com Streamlit
- Visualização de preços e dividendos
- Análise gráfica em tempo real

## Tecnologias Principais
- Python 3.x
- Pandas
- Streamlit
- Plotly

## Início Rápido
1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute cada desafio seguindo as instruções em seus respectivos READMEs

## Links Úteis
- Dashboard online: [FII Dashboard App](https://dashboardfiis.streamlit.app/)
- Documentação detalhada disponível nos READMEs individuais de cada desafio