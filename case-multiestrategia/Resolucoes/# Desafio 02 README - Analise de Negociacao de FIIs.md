# Análise de Negociação de FIIs

## Sobre o Projeto
Este projeto tem como objetivo analisar dados de negociação de Fundos de Investimento Imobiliário (FIIs). Ele realiza tarefas como:

- Carregar dados de negociações de FIIs a partir de um arquivo Excel.
- Identificar o FII com o maior volume negociado em um único dia.
- Determinar o dia com o maior volume total negociado em um período específico (ex.: ano de 2024).

## Estrutura do Projeto
```
projeto/
├── dados/
│   ├── negociacao_fiis.xlsx
│   └── carteira_ifix.xlsx
├── Desafio02.ipynb
└── README.md
```

## Pré-requisitos
- Python 3.8 ou superior
- Editor de código ou ambiente de desenvolvimento compatível (recomendado: VSCode ou Jupyter Notebook)

## Bibliotecas Necessárias
Execute os seguintes comandos para instalar as dependências:

```bash
pip install pandas
pip install openpyxl
```

## Configuração
1. Certifique-se de que os arquivos `negociacao_fiis.xlsx` e `carteira_ifix.xlsx` estejam presentes no diretório `dados/`.
2. Atualize o caminho dos arquivos no código, caso necessário, para refletir o local correto em seu sistema.

Exemplo de atualização do caminho:
```python
FILE_PATH = r'C:\caminho\para\negociacao_fiis.xlsx'
```

3. Certifique-se de que o arquivo possui dados formatados corretamente, incluindo uma coluna `dt_pregao` com datas.

## Uso
### Funcionalidade 1: Carregar dados de negociação
```python
df_negociacao = carregar_dados_negociacao()
```
### Funcionalidade 2: Encontrar FII com maior volume negociado
```python
fii_max, date_max, volume_max = encontrar_fii_maior_volume(df_negociacao)
print(f"FII com maior volume negociado: {fii_max}")
```

### Funcionalidade 3: Encontrar o dia com maior volume total em 2024
```python
max_daily_date, max_daily_volume = encontrar_maior_volume(df_negociacao)
print(f"Dia com maior volume: {max_daily_date}")
```

### Funcionalidade 4: Calcular volume mensal do IFIX
```python
df_ifix = carregar_dados_ifix()
monthly_ifix_volume = calcular_volume_ifix_por_mes(df_negociacao, df_ifix)
```

### Funcionalidade 5: Calcular percentual do IFIX no dia de maior volume
```python
ifix_percentage = calcular_percentual_ifix(df_negociacao, df_ifix, max_daily_date, max_daily_volume)
print(f"Percentual do IFIX: {ifix_percentage:.2f}%")
```

## Resultados Esperados
- Nome do FII com maior volume negociado em um dia.
- Data e volume negociado.
- Dia e volume total negociado mais alto no ano de 2024.

## Notas
- Certifique-se de que os arquivos de dados estejam no formato correto.
- A execução do projeto depende dos caminhos dos arquivos estarem configurados corretamente.

