# 빙산
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 데이터 받기
N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

# 빙산의 개수 세기
def cnt_icebergs():
    def DFS(row, col):
        visited[row][col] = True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if not visited[row + dr][col + dc] and G[row + dr][col + dc] > 0:
                DFS(row + dr, col + dc)
    
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if G[i][j] > 0 and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    return cnt

# 1년 뒤 빙산 시뮬레이션
def next_year():
    global G
    temp = [[0] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if G[i][j] > 0:
                sea = 0
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if G[i + dr][j + dc] <= 0:
                        sea += 1
                temp[i][j] = max(0, G[i][j] - sea)
    G = temp

year = 0
while True:
    year += 1
    next_year()
    icebergs = cnt_icebergs()
    if icebergs <= 0:
        print(0)
        break
    elif icebergs > 1:
        print(year)
        break