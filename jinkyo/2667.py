import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [ [0]*n for _ in range(n)]

direction = [[1,0], [0,1],[-1,0],[0,-1]]

def dfs(position, visited): #position = [x,y] 처음 발견한 개수 반환하는 함수
    stack = deque()
    stack.append(position)
    x, y = position
    visited[x][y] = 1
    count = 1 # 연결된 개수 세기

    while stack:
        a, b = stack.pop()
        for i in range(4):
            nx = a + direction[i][0]
            ny = b + direction[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: #범위 밖이면 제외
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                visited[nx][ny] = 1
                stack.append([nx,ny])
    return count

data=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] ==1 and visited[i][j]==0:
            a = dfs((i, j), visited)
            data.append(a)

print(len(data))
data.sort()
print(*data, sep='\n')
