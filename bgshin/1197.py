#  그래프 탐색 기본 (하) - 최소 스패닝 트리

import sys

# 크루스칼 알고리즘
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, sys.stdin.readline().split())
parent = [i for i in range(V + 1)]
edges = []

for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


# 프림 알고리즘
import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False] * (V + 1)
queue = [(0, 1)]  # (cost, vertex)
result = 0

while queue:
    cost, vertex = heapq.heappop(queue)

    if not visited[vertex]:
        visited[vertex] = True
        result += cost

        for next_cost, next_vertex in graph[vertex]:
            if not visited[next_vertex]:
                heapq.heappush(queue, (next_cost, next_vertex))

print(result)
