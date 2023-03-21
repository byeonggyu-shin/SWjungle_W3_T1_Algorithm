#  BFS (중) - 미로 만들기

import sys
import heapq

# 미로의 크기 n
n = int(sys.stdin.readline())
# 미로 정보 입력
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 상, 하, 좌, 우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 다익스트라 알고리즘
def dijkstra():
    distance = [[float('inf')] * n for _ in range(n)]
    distance[0][0] = 0
    q = []
    heapq.heappush(q, (0, 0, 0))  # (거리, x 좌표, y 좌표)
    while q:
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        # 상, 하, 좌, 우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위를 벗어나지 않을 때
            if 0 <= nx < n and 0 <= ny < n:
                # 만약 검은 방을 지나면 1이 더해짐
                cost = dist + (1 - maze[nx][ny])
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance[n - 1][n - 1]

result = dijkstra()
print(result)