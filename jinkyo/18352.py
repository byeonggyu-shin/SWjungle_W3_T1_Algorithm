from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

#단방향임!
adj_list = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)

distance = [-1]*(n+1)

def bfs(node, k):  # x는 시작점, k는 원하는 깊이
    queue = deque([node])
    distance[node] = 0
    result = []

    while queue:
        v = queue.popleft()
        for i in adj_list[v]:
            if distance[i]==-1:
                distance[i] = distance[v]+1
                queue.append(i)

    for i in range(1, n+1):
        if distance[i] == k:
            result.append(i)
    return result

a = bfs(x, k)


if len(a) == 0:
    print(-1)
else:
    print(*a, sep='\n')








