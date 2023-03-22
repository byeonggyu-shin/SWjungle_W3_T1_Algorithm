# graph , DFS , bFS  - 유기농 배추

import sys
from collections import deque

t =int(sys.stdin.readline())

def cabbageFram():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y):
        visited[x][y] = True
        q = deque([(x, y)]) 
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if farm[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    
    m,n,k = map(int, sys.stdin.readline().split())
    farm = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        farm[b][a] = 1

    worm = 0
    for i in range(m):
        for j in range(n):
            if farm[j][i] != 0 and not visited[j][i]:
                bfs(j,i)
                worm +=1

    return worm

for _ in range(t):
    print(cabbageFram())