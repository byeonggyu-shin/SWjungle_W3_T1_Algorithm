#연결 요소의 개수

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

#정점n, 간선m
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문했는지 확인 table
visited = [False]*(n+1)
#연결 요소 count변수
count = 0

def dfs(start):
    global count
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)
