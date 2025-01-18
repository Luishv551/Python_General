n = int(input())

numeros = []


for i in range (n):
    x = int(input())
    numeros.append(x)

numeros_processados = {}

for numero in numeros:
    if numero in numeros_processados:
        numeros_processados[numero] += 1
    else:
        numeros_processados[numero] = 1

numeros_ordenados = sorted(numeros_processados.keys())

for numero in numeros_ordenados:
    print(f"{numero} aparece {numeros_processados[numero]} vez(es)")



     