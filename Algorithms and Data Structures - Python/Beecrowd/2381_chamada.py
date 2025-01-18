N, K = map(int, input().split())

K -= 1
nomes = []

for i in range(N):
        nome = input()
        nomes.append(nome)

nomes.sort()

print(nomes[K])