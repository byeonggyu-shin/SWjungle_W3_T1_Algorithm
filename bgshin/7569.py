#  BFS (중) - tomato

import sys
from collections import deque

def bfs():
    # 박스에 토마토가 있다면
    while queue:
        # 3차원인 박스, 3개 축에서 하나씩뺌
        x, y, z = queue.popleft()

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz

            # 상하좌우 범위를 벗어나지 않고 토마토가 익지 않았다면
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and boxes[nx][ny][nz] == 0:
                # bfs들어오기 전 자리 +1  로 할당  
                boxes[nx][ny][nz] = boxes[x][y][z] + 1
                queue.append((nx, ny, nz))

m, n, h = map(int, sys.stdin.readline().split())
boxes = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)]for _ in range(h)]

directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

queue = deque()

# 큐에 익은 토마토 넣고
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                queue.append((i, j, k))
# 일단 bfs 돌려서 모든 토마토 익게 만듦
bfs()

max_days = 0
is_possible = True
# 다시 for 문으로 다 익었는지 확인 아직 익지 않은 토마토가 있다면 false, 
# 모든 자리 체크해서 날짜 비교
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                is_possible = False
                break
            max_days = max(max_days, boxes[i][j][k])

if is_possible:
    print(max_days - 1)
else:
    print(-1)