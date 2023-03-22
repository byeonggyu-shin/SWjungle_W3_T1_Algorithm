#  DFS (상) - 빙산

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 방문기록
    visited[x][y] = True
    # 현재위치 업데이트
    q = deque([(x, y)])

    # 주변 모든 빙산이 다 녹아서 없을떄까지 반복
    while q:
        cnt = 0
        x, y = q.popleft()
        # 상하좌우에
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 넘어가지 않고
            if 0 <= nx < n and 0 <= ny < m:
                # 바다이고 방문한적이 없다면
                if iceberg[nx][ny] == 0 and not visited[nx][ny]:
                    cnt += 1
                # 얼음이고 방문한 적이 없다면
                elif iceberg[nx][ny] > 0 and not visited[nx][ny]:
                    # 옆에 얼음도 방문 기록
                    visited[nx][ny] = True
                    # 옆에 얼음도 bfs을 위해 큐에 추가
                    q.append((nx, ny))
        # 빙산이 다 녹을떄까지 시간 최소 0
        iceberg[x][y] = max(0, iceberg[x][y] - cnt)


year = 0

while True:
    group = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # 얼음이고 방문한적 없는 경우
            if iceberg[i][j] != 0 and visited[i][j]==False:
                bfs(i,j)
                group +=1
    year +=1

    if group >= 2:
        print(year-1)
        break
    elif group == 0:
        print(0)
        break