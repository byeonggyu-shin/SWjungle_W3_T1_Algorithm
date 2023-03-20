#최소 스패닝 트리
import heapq
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기 / 시작은 자기 자신만 집합
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

#노드의 개수 v, 와 간선의 개수e 입력받기
v, e = map(int, input().split())

# parent [0, 1, 2, 3]
# 부모 테이블 상에서 부모를 자기 자신으로 초기화
parent = [0] * (v + 1)
for i in range(1, v+1):
    parent[i]=i

#모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    #비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b))
# [(1, 1, 2), (2, 2, 3), (3, 1, 3)]
#간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        print(parent)

print(result)

# 프림알고리즘
input = sys.stdin.readline

v, e = map(int, input().split())
cnt, hq = 0, []
visit = [0]*(v+1)

# 무방향 그래프 구성
link = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    link[a].append((c, b))
    link[b].append((c, a))

# 임의의 정점을 힙에 넣음
visit[1] = 1
for i in link[1]:
    heapq.heappush(hq, i)

result = 0
while hq:
    # 간선이 총 v-1개 이루어졌다면 종료
    if cnt == v-1:
        break

    w, node = heapq.heappop(hq)
    if visit[node]:
        continue

    cnt += 1
    result += w
    visit[node] = 1
    for i in link[node]:
        tw, tnode = i
        if visit[tnode]:
            continue
        heapq.heappush(hq, i)
print(result)
