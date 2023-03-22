# 위상정렬 - 문제집

import sys , heapq

n ,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)  # 진입 차수

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = []
# 문제 1 부터 n+1 번까지
for i in range(1, n + 1):
    # 진입차수 0인걸로 시작
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    result.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

print(" ".join(map(str, result)))