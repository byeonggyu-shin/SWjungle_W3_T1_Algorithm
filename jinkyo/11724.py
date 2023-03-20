#연결 요소의 개수

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
count = 0

def dfs(node, visited):
    visited[node] = 1
    
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i, visited)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i,visited)
        count+=1

print(count)


