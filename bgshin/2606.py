# 그래프 탐색 기본 (하) - 바이러스

import sys
sys.setrecursionlimit(10**6)  

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []

def dfs(graph, start_node):
    global visited
    visited.append(start_node)
    for i in graph[start_node]:
        if i not in visited:
            dfs(graph, i)
    return visited

dfs(graph, 1)
if len(visited):  
    print(len(visited)-1)
else:
    print(0)





#  무조건 1번 컴퓨터가 바이러스에 걸림