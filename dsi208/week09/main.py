import heapq

def dijkstra(graph, start):
    # Initialize distances for all vertices
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to hold vertices to be processed
    pq = [(0, start)]

    while pq:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the PQ multiple times. We only
        # process a vertex the first time we remove it from the PQ.
        if current_distance > distances[current_vertex]:
            continue

        # Consider neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Graph representation
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3), ('E', 4)],
    'D': [('E', 1)],
    'E': []
}


# Find shortest paths from A
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from {start_node}:")
for destination, distance in shortest_paths.items():
    print(f"{start_node} -> {destination}: {distance}")