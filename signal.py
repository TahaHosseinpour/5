import heapq
from collections import defaultdict
import sys

def dijkstra(n, graph):
    distances = [float('inf')] * (n + 1)
    distances[1] = 0
    min_heap = [(0, 1)]  # (distance, node)

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    max_distance = 0
    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            return -1
        max_distance = max(max_distance, distances[i])

    return max_distance

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    result = dijkstra(n, graph)
    print(result)

if __name__ == "__main__":
    main()
