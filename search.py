from collections import defaultdict

def floyd_warshall(edges):
    graph = defaultdict(dict)
    INF = float('inf')

    nodes = set()
    for u, v, weight in edges:
        nodes.add(u)
        nodes.add(v)
        if v not in graph[u]:
            graph[u][v] = weight
        else:
            graph[u][v] = min(graph[u][v], weight)

    dist = {node: {other: INF for other in nodes} for node in nodes}
    for node in nodes:
        dist[node][node] = 0

    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def floyd_cost(dist, start, target):
    if start not in dist or target not in dist[start]:
        return float('inf')
    return dist[start][target]

n, m = map(int, input().split())
first_list = input().strip()
scnd_list = input().strip()

node_list1 = input().split()
node_list2 = input().split()
edge_weight = map(int, input().split())

edges = [(node_list1[i], node_list2[i], w) for i, w in enumerate(edge_weight)]

distances = floyd_warshall(edges)

total_cost = 0

for start, target in zip(first_list, scnd_list):
    cost = floyd_cost(distances, start, target)
    if cost == float('inf'):
        print(-1)
        exit(0)
    total_cost += cost

print(total_cost)
