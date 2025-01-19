from collections import deque, defaultdict

n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
maxFee = int(input())

graph = defaultdict(list)
for road in roads:
    u, v, fee = road
    if fee <= maxFee:
        graph[u].append((v, fee))
        graph[v].append((u, fee))


def bfs(start):
    visited = [False] * n
    visited[start] = True
    queue = deque([start])
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor, fee in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count


min_neighbors = n + 1
best_village = -1

for i in range(n):
    neighbor_count = bfs(i)

    if neighbor_count < min_neighbors or (neighbor_count == min_neighbors and i > best_village):
        min_neighbors = neighbor_count
        best_village = i

print(best_village)
print("Hello")
