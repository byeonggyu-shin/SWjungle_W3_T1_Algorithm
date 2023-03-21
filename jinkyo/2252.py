import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split()) #n은 학생수, m은 키를 비교한 횟수

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]  # [[], [3], [3], []]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q= deque()
    
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-= 1
            if indegree[i]==0:
                q.append(i)

    print(*result)

topology_sort()    