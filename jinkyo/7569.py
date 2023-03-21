#토마토
# bfs

import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append([list(map(int, input().split())) for _ in range(n)])
# 여기까지가 input

# 사용할 변수들
# dir[h][n][m] n은 row,x m은 col,y
dir = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0],
       [0, 0, 1], [0, 0, -1]]  # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤

node_list = []

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                node_list.append((i, j, k))
# print(node_list)  # [(0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4)]


def bfs(node_list, graph):
    day = -1  # day 초기값 -1로 설정
    queue = deque()
    for i in node_list:
        queue.append(i)
    while queue:
        size = len(queue)
        for _ in range(size):
            z, x, y = queue.popleft()
            for i in range(6):
                nx = x + dir[i][1]
                ny = y + dir[i][2]
                nz = z + dir[i][0]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                    continue
                if graph[nz][nx][ny] == 1 or graph[nz][nx][ny] == -1:
                    continue
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    queue.append((nz, nx, ny))
        day += 1  # 모든 노드가 하루가 지나면 day를 1 증가시킴

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
    return day


result = bfs(node_list, graph)
print(result)
