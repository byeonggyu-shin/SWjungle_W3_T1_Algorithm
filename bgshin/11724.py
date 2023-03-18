# 그래프 탐색 기본 (하) - 연결 요소의 개수

import sys


n,m =map(int, sys.stdin.readline().split())

# 주어진 노드와 간선 정보를 이용하여 그래프 생성
# ex)  인접 리스트, 인접 행렬, 딕셔너리 등 다양한 방식을 사용할 수 있다 , 여기선 인접행렬 사용
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (n + 1)
connected_components = 0


def dfs(graph, node):
    
    global visited

    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor)


# 모든 노드를 순회하면서 아직 방문하지 않은 노드를 시작점으로 깊이 우선 탐색(DFS) 또는 너비 우선 탐색(BFS)을 수행합니다.
for node in range(1, n+1):
    if not visited[node]:
        dfs(graph, node)
        # DFS나 BFS를 수행할 때마다 연결 요소의 개수를 증가시킵니다.
        connected_components += 1
# 모든 노드에 대해 탐색이 완료되면, 연결 요소의 개수를 출력
print(connected_components)




