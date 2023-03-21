#  BFS (중) - 탈출

import sys
from collections import deque

def bfs(cnt):
    # 물이 차오름
    while water and docci:
        
        water_cnt = len(water)
        for _ in range(water_cnt):
            x, y = water.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위를 벗어나지 않고 돌도 없다면
                # 물을 채우고 큐에 넣음
                if 0 <= nx < c and 0 <= ny < r and forest[nx][ny] != 'X' and forest[nx][ny] != 'D'  and forest[nx][ny] != '*':
                    forest[nx][ny] = '*'
                    water.append((nx, ny))
                # 물이 한칸 먼저 차면 도치가 달림 (차오르면 못가기 때문)

        docci_cnt = len(docci)
        for _ in range(docci_cnt):
            a,b = docci.popleft()
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if na == end[0] and nb == end[1]:
                    return cnt+1
                # 도치는 물도 안됨
                if 0 <= na < c and 0 <= nb < r and forest[na][nb] != 'X' and forest[na][nb] != '*':
                    docci.append((na, nb))
                    forest[na][nb] = 'S'
        cnt += 1
    # 갈대 없으면 죽어야지    
    return('KAKTUS')    

r, c = map(int, sys.stdin.readline().split())

forest = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

water = deque()
docci = deque()
# 물을 큐에 넣고 시작 끝점 위치 변수에 저장 
for i in range(r):
    for j in range(c):
        if forest[i][j] == "*":
            water.append((i,j))
        elif forest[i][j] == "S":
            docci.append([i,j])
        elif forest[i][j] == "D":
            end = [i,j]


cnt = 0
print(bfs(cnt))



# import sys
# from collections import deque

# def bfs(cnt):
#     while water and docci:
#         # 물이 차오름
#         qlen = len(water)
#         for _ in range(qlen):
#             x, y = water.popleft()

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if 0 <= nx < c and 0 <= ny < r and forest[nx][ny] != 'X' and forest[nx][ny] != '*':
#                     forest[nx][ny] = '*'
#                     water.append((nx, ny))

#         qlen = len(docci)
#         for _ in range(qlen):
#             a, b = docci.popleft()

#             for i in range(4):
#                 na = a + dx[i]
#                 nb = b + dy[i]

#                 if na == end[0] and nb == end[1]:
#                     return cnt + 1
#                 if 0 <= na < c and 0 <= nb < r and forest[na][nb] != 'X' and forest[na][nb] != '*' and forest[na][nb] != 'S':  
#                     docci.append((na, nb))
#                     forest[na][nb] = 'S'
#         cnt += 1

#     return 'KAKTUS'

# r, c = map(int, sys.stdin.readline().split())

# forest = [list(input().strip()) for _ in range(r)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# water = deque()
# docci = deque()
# for i in range(r):
#     for j in range(c):
#         if forest[i][j] == "*":
#             water.append((i, j))
#         elif forest[i][j] == "S":
#             docci.append([i, j])
#         elif forest[i][j] == "D":
#             end = [i, j]

# cnt = 0
# print(bfs(cnt))