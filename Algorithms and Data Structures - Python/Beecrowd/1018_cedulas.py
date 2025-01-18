reais = int(input())
reais_f = reais

notas100 = reais // 100
reais = reais % 100

notas50 = reais // 50
reais = reais % 50

notas20 = reais // 20
reais = reais % 20

notas10 = reais // 10
reais = reais % 10

notas5 = reais // 5
reais = reais % 5

notas2 = reais // 2
reais = reais % 2

print(reais_f)
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{reais} nota(s) de R$ 1,00")

#SOLUCAO ELEGANTE

reais = int(input())
reais_f = reais

notas = [100, 50, 20, 10, 5, 2, 1]
resultados = {}

for nota in notas:
    resultados[nota] = reais // nota
    reais %= nota

print(reais_f)
for nota in notas:
    print(f"{resultados[nota]} nota(s) de R$ {nota},00")

