def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = set(graph)

    while unvisited:
        min_node = None
        min_distance = float('inf')
        for i in unvisited:
            if distances[i] < min_distance:
                min_node = i
                min_distance = distances[i]
        if min_node == None:
            break

        unvisited.remove(min_node)

        for neighbor, weight in graph[min_node].items():
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    return distances


graph = {
    'A': {'B': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 6},
    'D': {'B': 1, 'C': 4, 'E': 2, 'F': 8},
    'E': {'C': 6, 'D': 2, 'F': 7},
    'F': {'D': 8, 'E': 7}
}
start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)
