lista = {}

while True:
    try:
        item = input()

        item = item.upper()
        if item in lista:
            lista[item] += 1
        else:
            lista[item] = 1

    except EOFError:
        break

for key in sorted (lista.keys()):
    print(lista[key], key)
