# 위상정렬 - 음악 프로그램

import sys 
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

q = deque()

for _ in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    # 가수들이 부르는 곡의 순서를 그래프
    for i in range(1,data[0]):
        a,b =data[i], data[i+1]
        graph[a].append(b)
        # 진입차수 설정
        indegree[b] += 1

result = []
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
# 그냥 순서대로 간선대로 타고 들어가서
while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

# 모든 노드를 방문했다면 결과 출력, 아니라면 0 출력
if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)
