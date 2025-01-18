from random import sample

ms = {7, 13, 17, 33, 41, 58}
acertos = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for _ in range(10000):
    jogada = set(sample(range(1, 61), 6))
    acertos[len(jogada & ms)] += 1

for chave, valor in acertos.items():
    print(f'{chave} acerto(s): {valor}')
