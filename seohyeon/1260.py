# DFS와 BFS
import sys
input = sys.stdin.readline

def DFS(start):
    visited[start] = True
    dfs_ans.append(start)
    for v in sorted(G[start]):
        if not visited[v]:
            DFS(v)

def BFS(start):
    Q = [start]
    visited[start] = True
    while Q:
        u = Q.pop(0) # 왠지 모르겠지만 큐보다 리스트.pop(0)을 쓰니까 빨랐음
        bfs_ans.append(u)
        for v in sorted(G[u]):
            if not visited[v]:
                Q.append(v)
                visited[v] = True

N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

dfs_ans = []
bfs_ans = []

visited = [False] * (N + 1)
DFS(V)
visited = [False] * (N + 1)
BFS(V)

print(*dfs_ans)
print(*bfs_ans)