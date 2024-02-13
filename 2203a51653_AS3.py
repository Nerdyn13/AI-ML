import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    path = {}

    while heap:
        (dist, current) = heapq.heappop(heap)
        if current == end:
            break
        for neighbor, neighbor_dist in graph[current].items():
            old_dist = distances[neighbor]
            new_dist = dist + neighbor_dist
            if new_dist < old_dist:
                distances[neighbor] = new_dist
                path[neighbor] = current
                heapq.heappush(heap, (new_dist, neighbor))

    # Reconstruct the shortest path
    s, u = [], end
    while u != start:
        s.append(u)
        u = path[u]
    s.append(start)
    return distances[end], s[::-1]

# Define your graph here
graph = {
    '0': {'1': 4, '3': 3, '4': 2},
    '1': {'2': 4},
    '2': {'3': 7, '5': 5},
    '3': {},
    '4': {'1': 5, '5': 6},
    '5': {'2': 2},
    '6': {}
}

print(dijkstra(graph, '0', '5'))
