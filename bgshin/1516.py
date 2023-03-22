# 위상정렬 - 게임 개발

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)  # 건설 시간
indegree = [0] * (n + 1)  # 진입 차수
result = [0] * (n + 1)

for i in range(1,n+1):
    lst = list(map(int, sys.stdin.readline().split()))
    time[i] = lst[0]
    for j in lst[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

q = deque() 

for i in range(1, n + 1):           
    # 진입 차수가 0인걸 넣어준다.
    if indegree[i] == 0:
        q.append(i)
        # 진입할때 소요시간 기록
        result[i] = time[i]

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        # 현재 노드를 거쳐가는 시간을 갱신
        result[i] = max(result[i], result[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])
