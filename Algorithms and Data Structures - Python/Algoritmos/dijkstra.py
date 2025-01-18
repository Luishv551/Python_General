import heapq

def dijkstra(graph, start):
    # Inicializa as distâncias de todos os nós como infinito
    dist = {node: float('inf') for node in graph}
    dist[start] = 0  # Distância para o nó inicial é 0

    # Fila de prioridade para o heap
    prioridade = [(0, start)]

    while prioridade:
        # Extrai o nó com a menor distância atual
        dist_atual, nodo_atual = heapq.heappop(prioridade)

        # Se a distância atual for maior que a armazenada, ignora
        if dist_atual > dist[nodo_atual]:
            continue

        # Atualiza a distância dos vizinhos
        for vizinho, peso in graph[nodo_atual]:
            distancia = dist_atual + peso

            if distancia < dist[vizinho]:
                dist[vizinho] = distancia
                heapq.heappush(prioridade, (distancia, vizinho))

    return dist

# Definição do grafo com listas de tuplas
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

# Nó inicial
start = 'A'

# Executa o Dijkstra
menor_caminho = dijkstra(graph, start)

# Exibe os resultados
print("Menor distância de A para os outros nós:")
for nodo, distancia in menor_caminho.items():
    print(f"{nodo}: {distancia}")
