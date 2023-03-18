# 그래프 탐색 기본 (하) - DFS 와 BFS 

import sys
from collections import defaultdict , deque

n, m ,v =  map(int ,sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node].sort()



def dfs(graph, start_node, visited=[]):
    visited.append(start_node)
    for i in graph[start_node]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited

dfs_result = dfs(graph, v)
print(' '.join(map(str, dfs_result)))

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append(current_node)
            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)

    return visited

bfs_result = bfs(graph, v)
print(' '.join(map(str, bfs_result)))