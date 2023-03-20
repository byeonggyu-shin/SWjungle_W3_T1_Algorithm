# DFS (중) - 트리의 부모 찾기 

import sys
sys.setrecursionlimit(10**6)  

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 1번 노드를 루트로 설정합니다.
# 인접 리스트를 바탕으로, 1번 노드와 인접한 노드들을 탐색합니다.
# 각 노드를 방문하면서, 해당 노드의 부모를 1번 노드로 설정합니다.
# 각 노드의 자식 노드들을 재귀적으로 방문하면서, 해당 자식 노드의 부모를 현재 노드로 설정합니다.

def dfs(node, parent, graph, visited, result):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            result[child] = node
            dfs(child, node, graph, visited, result)

visited = [False] * (n+1)
result = [0] * (n+1)


dfs(1, 0, graph, visited, result)
print(result)
for i in range(2, n+1):
    print(result[i])