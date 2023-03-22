# 유기농 배추
from collections import deque
import sys

input = sys.stdin.readline

# t = int(input())
m, n, k = map(int,input().split()) #m가로길이, n세로길이, 배추 위치의 개수k

graph = [[0]*m for _ in range(n)]

for _ in range(k):
    b, a = map(int, input().split())
    graph[a][b]=1

visited = [[0]*m for _ in range(n)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs(position, visited, count):  # position = [x,y] 처음 발견한 개수 반환하는 함수
    queue = deque()
    queue.append(position)
    x, y = position
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + direction[i][0]
            ny = b + direction[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 범위 밖이면 제외
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                visited[nx][ny] = 1
                queue.append([nx, ny])
    return count

data = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            a = bfs((i,j), visited,0)
            data.append(a)

print(data)
