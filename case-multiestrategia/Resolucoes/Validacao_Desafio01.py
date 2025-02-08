import os
import pandas as pd
import logging

# Configuracao Base
BASE_DIR = r'C:\Users\luish\OneDrive\Área de Trabalho\Python Projetos\case-multiestrategia\dados\00_raw_data'
OUTPUT_DIR = os.path.join(BASE_DIR, 'Desafio 01')
CONSOLIDADO_FILE = os.path.join(OUTPUT_DIR, 'arquivo_final.xlsx')
LOG_FILE = os.path.join(OUTPUT_DIR, 'validacao.log')

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def contar_linhas_csv():
    total_linhas = 0
    arquivos_processados = 0

    for arquivo in os.listdir(BASE_DIR):
        if arquivo.startswith('IFIXDia_') and arquivo.endswith('.csv'):
            try:
                df = pd.read_csv(os.path.join(BASE_DIR, arquivo), skiprows=1)
                linhas_validas = len(df[df.iloc[:, 0] != 'Total'])
                
                total_linhas += linhas_validas
                arquivos_processados += 1
                
                logging.info(f'Arquivo {arquivo}: {linhas_validas} linhas válidas')
                
            except Exception as e:
                logging.error(f'Erro ao processar {arquivo}: {e}')

    return total_linhas, arquivos_processados

def validar():
    print('\nIniciando processo de validação...')
    logging.info('Iniciando validação')
    total_csv, arquivos = contar_linhas_csv()
    
    try:
        df_consolidado = pd.read_excel(CONSOLIDADO_FILE)
        total_consolidado = len(df_consolidado)
        
        logging.info(f'Registros nos CSVs: {total_csv:,}')
        logging.info(f'Registros no consolidado: {total_consolidado:,}')
        logging.info(f'Arquivos processados: {arquivos}')
        
        print(f'\nValidação concluída!')
        print(f'Total de registros nos arquivos CSV: {total_csv:,}')
        print(f'Total de registros no arquivo consolidado: {total_consolidado:,}')
        print(f'Diferença: {abs(total_csv - total_consolidado):,} registros')
        print(f'\nO arquivo de log foi salvo em: {LOG_FILE}')
            
        if total_csv != total_consolidado:
            logging.warning(f'Diferença encontrada: {abs(total_csv - total_consolidado):,} registros')
            print('\nATENÇÃO: Foi encontrada uma diferença entre os totais!')
            
    except Exception as e:
        logging.error(f'Erro na validação: {e}')
        print(f'Erro durante a validação: {e}')

if __name__ == '__main__':
    validar()