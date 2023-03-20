# 연결 요소의 개수
# 큐 대신 리스트 쓴 풀이(652ms)
"""BSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 BSF 돌리기
BSF 돌린 횟수를 출력"""

import sys
input = sys.stdin.readline

def BFS(start):
    Q = [start]
    visited[start] = True
    while Q:
        u = Q.pop(0) # 정점의 개수가 적어서인지 큐보다 리스트.pop(0)이 더 빠르다
        for v in G[u]:
            if not visited[v]:
                Q.append(v)
                visited[v] = True
            
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

visited = [False] * (N + 1)
visited[0] = True

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        BFS(i)
        cnt += 1
print(cnt)
