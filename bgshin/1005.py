# 위상정렬 - ACM Craft

import sys
from collections import deque

def toppology_sort(): 
    n, k = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)  # 진입 차수
    result = [0] * (n + 1)

    for _ in range(k):
        a,b = list(map(int, sys.stdin.readline().split()))
        graph[a].append(b)
        indegree[b] += 1

    end = int(sys.stdin.readline())

    q = deque() 

    for i in range(1, n + 1):           
        # 진입 차수가 0인걸 넣어준다.
        if indegree[i] == 0:
            q.append(i)
            # 진입할때 소요시간 기록
            result[i] = time[i-1]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            # 현재 노드를 거쳐가는 시간을 갱신
            result[i] = max(result[i], result[now] + time[i-1])
            if indegree[i] == 0:
                q.append(i)

    print(result[end])

t = int(sys.stdin.readline())

for _ in range(t):
   toppology_sort()