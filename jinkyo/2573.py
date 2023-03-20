"""
빙산
dfs
"""
import sys

n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

count_year = 0
while True:

    count_year += 1
    count_water = [[0 for _ in range(m)] for _ in range(n)]

    # 녹일 빙산 찾기
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == 0:
                            count_water[i][j] += 1

    # 빙산 녹임
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                arr[i][j] -= count_water[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0

    # 빙산 카운트
    dfs_count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                dfs_count += 1
                # 이어진 빙산 방문 처리
                visited[i][j] = True
                queue = [[i, j]]
                while queue:
                    p = queue.pop()
                    for k in range(4):
                        nx = p[0] + dx[k]
                        ny = p[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] > 0 and not visited[nx][ny]:
                                queue.append([nx, ny])
                                visited[nx][ny] = True

    # 종료 조건
    if dfs_count > 1:
        break

    # 모두 녹은 경우
    total = 0
    for i in arr:
        total += sum(i)

    if total == 0:
        print(0)
        exit()
print(count_year)

#gpt와 함께 짠 코드

# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []  # graph[행][열]
# for i in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)

# direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 동남서북


# def dfs(x, y, visited, sea):
#     visited[x][y] = True

#     for dx, dy in direction:
#         nx, ny = x+dx, y+dy
#         if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 이동 가능한 범위인지 확인
#             continue
#         if graph[nx][ny] == 0:
#             sea[x][y] += 1
#         elif not visited[nx][ny]:
#             dfs(nx, ny, visited, sea)


# def count_iceberg():
#     visited = [[False] * m for _ in range(n)]  # 방문 여부 체크
#     count = 0  # 빙산 개수
#     while True:
#         # 바다 칸 개수 세기
#         sea = [[0] * m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] != 0 and not visited[i][j]:  # 빙산이 있고, 아직 방문하지 않은 경우
#                     count += 1  # 빙산 개수 증가
#                     dfs(i, j, visited, sea)  # DFS 탐색 진행
#         if count == 0:  # 빙산이 없으면 종료
#             return 0
#         if count >= 2:  # 빙산이 두 개 이상이면 종료
#             return count

#         # 빙산 녹이기
#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] > sea[i][j]:
#                     graph[i][j] -= sea[i][j]


# print(count_iceberg())
    
