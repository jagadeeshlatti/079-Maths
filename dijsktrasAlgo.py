from heapq import heappush, heappop


def dijkstra(graph, start):
    distance = {start: 0}
    queue = [(0, start)]
    while queue:
        (dist, current) = heappop(queue)
        if current in graph:
            for neighbor in graph[current]:
                new_dist = dist + graph[current][neighbor]
                if neighbor not in distance or new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heappush(queue, (new_dist, neighbor))
    return distance


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start = 'D'

result = dijkstra(graph, start)
print("The shortest distance from", start, "to each node:", result)