#바이러스

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 정점n, 간선m
n = int(input())
m = int(input())

# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문했는지 확인 table
visited = [False]*(n+1)
#count 변수
count=-1

def dfs(start):
    global count
    visited[start] = True
    count +=1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count)