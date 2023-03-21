#  BFS (하) - 미로 탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def bfs(n,m,maze):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        # 0,0 을 꺼내면서 시작
        y, x = queue.popleft()

        # 끝에 도착하면 리탄
        if y == n-1 and x == m-1:
            return maze[y][x]

        # 4가지 방향으로 위치 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 끝을 넘지 않고 길이 있으며 방문하지 않은 경우
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1 and not visited[ny][nx]:
                #  방문한 곳 트루, 미로에 +1 , 큐에 현재 위치 저장
                visited[ny][nx] = True
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny, nx))
    # 모든 경우에 실패할 경우
    return -1


print(bfs(n, m, maze))

