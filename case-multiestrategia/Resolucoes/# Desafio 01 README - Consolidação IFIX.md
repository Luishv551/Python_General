# Desafio 01 - Consolidação IFIX

## Sobre o Projeto
Este projeto realiza a consolidação de dados do índice IFIX (Índice de Fundos de Investimentos Imobiliários) a partir de múltiplos arquivos CSV em um único arquivo Excel. O processo inclui validação dos dados e geração de logs para acompanhamento.

## Estrutura do Projeto
```
case-multiestrategia/
├── dados/
│   └── 00_raw_data/
│       └── Desafio 01/
├── Resolucoes/
│   ├── Desafio01.ipynb
│   └── Validacao_Desafio01.py
└── README.md
```

## Pré-requisitos
- Python 3.x
- pip (gerenciador de pacotes Python)

## Bibliotecas Necessárias
```bash
pip install pandas
pip install openpyxl
```

## Configuração
1. Clone o repositório ou baixe os arquivos
2. Modifique o `BASE_DIR` nos arquivos `Desafio01.ipynb` e `Validacao_Desafio01.py` para apontar para o seu diretório local
3. Certifique-se de que os arquivos CSV do IFIX estejam no diretório especificado em `BASE_DIR`

## Uso
### Para consolidar os dados:
Execute o notebook Jupyter:
```bash
jupyter notebook Resolucoes/Desafio01.ipynb
```

### Para validar os dados:
Execute o script de validação:
```bash
python Resolucoes/Validacao_Desafio01.py
```

## Resultados
- O arquivo consolidado será salvo como `arquivo_final.xlsx` no caminho
 
 case-multiestrategia\dados\00_raw_data\Desafio 01
 
- Logs de processamento serão gerados em:
  - `processamento.log` (consolidação)
  - `validacao.log` (validação)

- O resultado final do Desafio01 com as etapas:

  1 - Utilize o arquivo Excel dados/01_cleaned_data/cadastro_fiis.xlsx para adicionar uma coluna de CNPJ ao dataframe consolidado.
  
  2 - O resultado final deve corresponder ao arquivo dados/01_cleaned_data/carteira_ifix.xlsx.

  Está na pasta em case-multiestrategia\dados\00_raw_data\Desafio 01 e nomeado como Resultado_Final_Desafio01

## Notas
- Os arquivos CSV de entrada devem seguir o padrão de nomenclatura: `IFIXDia_DD-MM-YYYY.csv`
- O script trata automaticamente valores percentuais e remove linhas de totais
- Logs detalhados são gerados para rastreamento de possíveis erros