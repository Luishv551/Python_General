import math

def hamekame(entrada):
    # Utilizando o metodo .find pois entrada e uma string, com esse metodo posso encontrar qual a posicao na string que mek inicia
    indice_mek = entrada.find("mek")

    # Podemos usar o : para determinar que iremos desde o inicio ate o certo ponto
    antes_mek = entrada[:indice_mek]

    # Ou de ate o final a partir de certo ponto
    depois_mek = entrada[indice_mek+3:]
    
    qtd_as_antes = antes_mek.count('a')
    qtd_as_depois = depois_mek.count('a')
    
    # multiplicando a quantidade de 'a's antes e depois de "mek"
    multiplicacao = qtd_as_antes * qtd_as_depois
    
    resultado = "k" + "a" * multiplicacao
    print(resultado)

quantidade_casos = int(input())

for caso in range(quantidade_casos):
    entrada = input()
    hamekame(entrada)
