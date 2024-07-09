import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Função principal
def main():
    # Entrada de dados
    ticker1 = input("Digite o primeiro ticker: ").upper()
    ticker2 = input("Digite o segundo ticker: ").upper()
    valor_investido = float(input("Digite o valor investido total: "))
    
    # Entrada da data de compra
    data_compra = input("Digite a data de compra (AAAA-MM-DD): ")
    data_compra = datetime.strptime(data_compra, "%Y-%m-%d")
    
    # Data final é hoje
    data_hoje = datetime.today().strftime('%Y-%m-%d')
    
    # Dividir o valor investido igualmente
    valor_por_acao = valor_investido / 2
    
    # Obter dados históricos das ações
    dados1 = yf.download(ticker1 + ".SA", start=data_compra, end=data_hoje)
    dados2 = yf.download(ticker2 + ".SA", start=data_compra, end=data_hoje)
    
    # Verificar se os dados foram baixados corretamente
    if dados1.empty:
        print(f"Não foi possível obter dados para o ticker {ticker1}")
        return
    if dados2.empty:
        print(f"Não foi possível obter dados para o ticker {ticker2}")
        return
    
    # Calcular a quantidade de ações compradas
    qtd_acoes1 = valor_por_acao / dados1['Close'].iloc[0]
    qtd_acoes2 = valor_por_acao / dados2['Close'].iloc[0]
    
    # Calcular a rentabilidade em reais ao longo do tempo
    rentabilidade1 = dados1['Close'] * qtd_acoes1
    rentabilidade2 = dados2['Close'] * qtd_acoes2
    
    # Plotar o gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(rentabilidade1.index, rentabilidade1, label=f'Rentabilidade {ticker1}')
    plt.plot(rentabilidade2.index, rentabilidade2, label=f'Rentabilidade {ticker2}')
    plt.xlabel('Data')
    plt.ylabel('Rentabilidade em Reais')
    plt.title('Rentabilidade das Ações')
    plt.legend()
    plt.grid(True)
    plt.show()

# Chamada da função principal
if __name__ == "__main__":
    main()
