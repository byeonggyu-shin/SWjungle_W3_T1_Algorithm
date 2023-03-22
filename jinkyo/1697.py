import sys
from collections import deque

n, k = map(int, input().split())



def bfs(n, k):
    queue = deque([n])
    while queue:
        v = queue.popleft()




            