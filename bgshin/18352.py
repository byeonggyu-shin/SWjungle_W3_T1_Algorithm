#  BFS (하) - 미로 탐색

import sys
from collections import deque 

n, m, k, x = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

 
lst = [[] for _ in range(n+1)]
# 인접행렬 생성
for a,b  in edges:
    lst[a].append(b)

# 빙문 기록 저장 
visted = [False] * (n+1)
visted[x] = True
# x에서 부터 해당 idx의 노드까지의 최단거리 저장 
distances = [-1] * (n+1)
distances[x] = 0

queue = deque([x, 0]) 

while queue:
    node = queue.popleft()

    for next in lst[node]:
        if not visted[next]:
            #  방문기록
            visted[next] = True
            # 거리는 이전 위치보다 +1 민큼 길어지고
            distances[next] = distances[node] + 1
            # 큐에 넣어서 현재 위치 업데이트
            queue.append(next)
    
    
result = [i for i, d in enumerate(distances) if d == k]

if result:
    for i in result:
        print(i)
else:
    print(-1)



