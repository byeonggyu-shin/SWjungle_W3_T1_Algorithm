# graph , DFS , bFS - 단지번호붙이기

import sys
from collections import deque

n = int(sys.stdin.readline())
home = [list(str(sys.stdin.readline())) for _ in range(n+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    cnt = 1   
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 안 이고 
            if 0 <= nx < n and 0 <= ny < n:
                # 집이면 방문하고 숫자세고
                if int(home[nx][ny]) == 1 and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return cnt
       
  
group = 0
result = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if int(home[i][j]) != 0 and not visited[i][j]:
            result.append(bfs(i,j))
            group +=1

print(group)
result.sort()
for i in result:
    print(i)