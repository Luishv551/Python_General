# Ordene uma string sem utilizar metodos built in

# tentativa 01

string = "14352698"

lista = list(string)


for i in range(len(lista) - 1):

    for j in range(i + 1, len(lista)):

        if lista[i] > lista[j]:

            lista[i], lista[j] = lista[j], lista[i]

            print(lista)

