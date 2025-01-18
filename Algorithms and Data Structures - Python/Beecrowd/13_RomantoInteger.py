#LEETCODE

romano_para_inteiro = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

def romano_para_inteiro(numero_romano):
    
    numero = 0
    i = len(numero_romano) - 1

    while i >= 0:

        #aqui coloco i > 0 pois se ja estiver na posicao 0 nao vai ter nada antes dele

        # i + 1 pois ele nao e inclusivo 
        if i > 0 and numero_romano[i-1:i+1] in romano_para_inteiro: 

            numero += romano_para_inteiro[numero_romano[i-1:i+1]] # slicing de string

            i -= 2  

        else:

            numero += romano_para_inteiro[numero_romano[i]]

            i -= 1

    return numero