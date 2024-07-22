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
    
    divisao = qtd_as_antes / qtd_as_depois
    
    total_as = entrada.count('a')

    if divisao > 1:

        adicao = math.ceil(total_as + divisao)

    else:

        adicao = int(divisao)
    
    resultado = "k" + "a" * adicao
    print(resultado)

quantidade_casos = int(input())

for _ in range(quantidade_casos):
    entrada = input()
    hamekame(entrada)
