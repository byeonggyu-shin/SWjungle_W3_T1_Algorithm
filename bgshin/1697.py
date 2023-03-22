# BFS - 숨바꼭질

import sys 
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = [0] * (2 * k + 1)
q = deque([n])
visited[n] = 1

while q:
    cur = q.popleft()
    
    if cur == k:
        print(visited[cur] - 1)

    for next in (cur - 1, cur + 1, cur * 2):
        if 0 <= next < len(visited) and not visited[next]:
            visited[next] = visited[cur] + 1
            q.append(next)


