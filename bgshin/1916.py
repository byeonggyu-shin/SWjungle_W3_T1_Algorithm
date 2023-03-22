#  BFS (중) - 최소 비용 구하기

import sys
import heapq

def dijkstra(start):
  #  초기값 무한대로 설정
  distance = {node: float('inf') for node in graph}
  # 시작점 초기화
  distance[start] = 0
  q = [(0, start)]

  # 큐에 인자 없을때까지 반복 <= 모든 노드가 반복됬을떼
  while q:
    #  현재 거리 , 노드 할당
    cur_dist, cur_node = heapq.heappop(q)
    #  거리가 크다면 최소값보다 커지니 넘어가면됨
    if distance[cur_node] < cur_dist:
        continue
    
    #  해당 노드의 엣지에서 이웃노드와 가중치를 가져와서 
    for neighbor, weight in graph[cur_node]:
        # 현재 거리에 지금까지의 가중치와 이번 엣지의 가중치를 더함
        dist = cur_dist + weight
        # 더한 값이 옆 노드의 가중치보다 작다면 <= 이쪽 방향이 더 작은 가중치를 가지고있음
        if dist < distance[neighbor]:
          #  작은값으로 재할당
           distance[neighbor] = dist
          # 힙에 다음 루트를 추가
           heapq.heappush(q, (dist, neighbor))

  return distance

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
                                                               
dpr , arv = map(int, sys.stdin.readline().split())


# 시간 초과 => graph를 생성할 때 간선이 중복되어 추가될 수 있다. 이를 수정하여 시간을 절약

# for node in graph:
#     neighbors = {}
#     for neighbor, weight in graph[node]:
#         if neighbor in neighbors:
#             neighbors[neighbor] = min(neighbors[neighbor], weight)
#         else:
#             neighbors[neighbor] = weight
#     graph[node] = [(k, v) for k, v in neighbors.items()]


distance = dijkstra(dpr)
print(distance[arv])



# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5