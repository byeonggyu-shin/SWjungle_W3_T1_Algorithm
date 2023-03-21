# 위상정렬 (중) - 장난감 조립

# import sys
# from collections import defaultdict , deque

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# # 위상정렬 모든 노드 진입차수기록
# indegree = [0] * (n + 1)

# graph = [[] for _ in range(n + 1)]
# # 비용을 딕셔너리로 따로 기록
# cost = [defaultdict(int) for _ in range(n + 1)]
# # 방향 그래프의 모든 간선 정보를 입력 받기
# for _ in range(m):
#     x, y ,k= map(int , sys.stdin.readline().split())
#     graph[y].append(x)
#     indegree[x] += 1
#     # y -> x 의 비용 저장해두고
#     cost[y][x] = k

# q = deque() 

# for i in range(1, n + 1):
#     # 진입 차수가 0인 기본 부품을 큐에 추가
#     if indegree[i] == 0:  
#         q.append(i)

# while q:
    
#     cur = q.popleft()

#     for next_node in graph[cur]:
#         # 연될된 노드들 진입차수 빼주고
#         indegree[next_node] -= 1
#         # 지금 부품 수에 곱한수 더해주고
#         for item, count in cost[cur].items():
            

#             cost[next_node][item] += count * cost[cur][next_node]
#         # 0이 되면 큐에 넣음
#         if indegree[next_node] == 0:
#             q.append(next_node)

# print(cost[n])

# for item, count in sorted(cost[n].items()):
#     print(item, count)

import sys
from collections import deque

n = int(sys.stdin.readline())

connect = [[] for _ in range(n + 1)]  # 연결 정보

needs = [[0] * (n + 1) for _ in range(n + 1)]  # 각 제품을 만들때 필요한 부품

q = deque()  # 위상 정렬

degree = [0] * (n + 1)  # 진입 차수

for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    connect[b].append((a, c))
    degree[a] += 1

for i in range(1, n + 1):
    # 진입 차수가 0인걸 넣어준다.
    if degree[i] == 0:
        q.append(i)
# 위상 정렬 시작
while q:
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지    
    for next, next_need in connect[now]:
        # 만약 현 제품이 기본 부품이면
        if needs[now].count(0) == n + 1:
            needs[next][now] += next_need
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, n + 1):
                needs[next][i] += needs[now][i] * next_need
        # 차수 -1
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0이면 큐에 넣음
            q.append(next)

for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)

