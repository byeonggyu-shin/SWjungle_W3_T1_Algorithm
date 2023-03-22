"""
빙산
dfs
"""
# 내코드 - 시간초과
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
year = -1


def dfs(x, y, visited, melt_candidates):
    visited[x][y] = 1
    for i in range(4):
        nx = x + direction[i][0]
        ny = y + direction[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            melt_candidates.append((x, y))
        elif graph[nx][ny] != 0 and visited[nx][ny] == 0:
            dfs(nx, ny, visited, melt_candidates)


while True:
    year += 1
    visited = [[0]*m for _ in range(n)]
    count = 0
    melt_candidates = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] != 0:
                count += 1
                dfs(i, j, visited, melt_candidates)
        for (x, y) in melt_candidates:
            graph[x][y] = max(0, graph[x][y]-1)
        melt_candidates = []
        if count >= 2:
            print(year)
            sys.exit()
    if count == 0:
        print(0)
        sys.exit()


# import sys
# input = sys.stdin.readline
# from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# year = -1

# def dfs(position, visited): #position = [x,y] 처음 발견한 빙산의 연결된 빙판 개수 반환하는 함수
#     stack = deque()
#     stack.append(position)
#     x, y = position
#     visited[x][y] = 1
#     count = 1 # 연결된 빙판 개수 세기
    
#     while stack:
#         a, b = stack.pop()
#         for i in range(4):
#             nx = a + direction[i][0]
#             ny = b + direction[i][1]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m: #범위 밖이면 제외
#                 continue
#             if graph[nx][ny] != 0 and visited[nx][ny] == 0:
#                 count += 1
#                 visited[nx][ny] = 1
#                 stack.append([nx,ny])
#     return count

# visited = [[0]*m for _ in range(n)]

# def first_search():
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] != 0 :
#                 return [i,j]

# print(dfs(first_search(), visited))

# #1년뒤 빙판 녹이는 함수
# def ice_melt():




