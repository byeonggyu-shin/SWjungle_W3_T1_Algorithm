# 바이러스
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

visited = [0] * (N + 1)

def DFS(node):
    visited[node] = 1
    for v in G[node]:
        if not visited[v]:
            DFS(v)

DFS(1)

print(sum(visited)-1)