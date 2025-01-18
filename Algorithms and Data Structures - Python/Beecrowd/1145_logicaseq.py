"""

ARGUMENTO: 3 99

RETORNO:

1 2 3
4 5 6
7 8 9
10 11 12
...
97 98 99

"""

import math

num = 0
quebra,i = map(int, input().split())

div = i / quebra

n_linhas = math.ceil(div)

for numero_na_linha in range (n_linhas):

    for operacao_de_soma in range (quebra):
        num = num + 1
        if operacao_de_soma < quebra -1 :
            print(f"{num} ", end="")
        else:
            print(f"{num}")
