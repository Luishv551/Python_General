# FII Dashboard

## Sobre o Projeto
Este projeto é um painel interativo desenvolvido com Streamlit para visualização de dados relacionados a Fundos de Investimento Imobiliário (FIIs). O dashboard permite:

- Carregar e exibir dados de negociação e dividendos de FIIs.
- Filtrar e visualizar informações de um FII selecionado.
- Gerar gráficos interativos de preço, volume negociado e dividend yield.

## Estrutura do Projeto
```
projeto/
├── dados/
│   ├── negociacao_fiis.xlsx
│   └── dividendos_fiis.xlsx
├── Desafio03.py
└── README.md
```

## Pré-requisitos
- Python 3.8 ou superior
- Editor de código ou ambiente de desenvolvimento compatível (recomendado: VSCode)

## Bibliotecas Necessárias
Execute os seguintes comandos para instalar as dependências:

```bash
pip install streamlit pandas plotly openpyxl
```

## Configuração
1. Certifique-se de que os arquivos `negociacao_fiis.xlsx` e `dividendos_fiis.xlsx` estejam presentes no diretório `dados/`.
2. Atualize o caminho dos arquivos no código, caso necessário, para refletir o local correto em seu sistema.

Exemplo de atualização do caminho:
```python
FILE_PATH = r'C:\caminho\para\negociacao_fiis.xlsx'
```

3. Certifique-se de que os arquivos de dados estejam formatados corretamente, com as colunas `dt_pregao` e `data_com` em formato de data.

## Uso
### Execução do Dashboard
Execute o seguinte comando no terminal para iniciar o aplicativo:

```bash
streamlit run Desafio03.py
```

### Funcionalidade 1: Carregar dados
Os dados são carregados automaticamente pelas funções definidas no script.

### Funcionalidade 2: Selecionar e visualizar dados de um FII
- Utilize o seletor de ticker para escolher o FII desejado.
- O painel exibirá:
  - Um gráfico com o preço de fechamento e volume negociado.
  - Um gráfico com o dividend yield anualizado.

## Resultados Esperados
- Gráfico interativo de preço e volume negociado.
- Gráfico interativo de dividend yield em porcentagem.

## Notas
- Certifique-se de que os arquivos de dados estejam no formato correto.
- O aplicativo pode ser acessado pelo navegador na porta padrão (geralmente `localhost:8501`).