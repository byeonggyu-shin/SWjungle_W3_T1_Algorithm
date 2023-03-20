#  BFS (하) - 미로 탐색

import sys
from collections import deque , defaultdict

n, m, k, x = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

road = defaultdict(list)
for edge in roads:
    a, b = edge
    road[a].append(b)

result = []
def bfs(k,x, cnt):
    
    global result

    cnt += 1
    if k == cnt:
        result = road[x]
    for i in road[x]:
        bfs(k,i,cnt)


bfs(k,x,cnt=0)

print(result)