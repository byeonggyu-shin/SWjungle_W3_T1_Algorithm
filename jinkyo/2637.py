#장난감 조립
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())  # 완제품 번호
indegree = [0] * (n + 1)  # 진입차수 table
graph = [[] for _ in range(n + 1)]  # 부품 정보 저장

m = int(input())  # 부품 정보 개수
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))  # y번 부품이 x번 부품에 k개 필요
    indegree[x] += 1  # y번 부품의 진입차수 증가

base_parts=[]
for i in range(len(indegree)):
    if indegree[i] == 0:
        base_parts.append(i)
# 위상 정렬 함수
def topology_sort():
    cnt = [0] * (n + 1)  # 각 부품의 필요한 총 개수를 기록하는 table
    q = deque()
    
    for i in range(1, n + 1):  # 진입차수가 0인 부품부터 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
            cnt[i] = 1  # 기본 부품의 필요한 개수는 1개
    while q:
        now = q.popleft()
        # 현재 부품과 연결된 부품들의 진입차수 감소 및 필요한 개수 업데이트
        for part, k in parts[now]:
            indegree[part] -= 1
            cnt[part] += cnt[now] * k  # 필요한 개수 업데이트
            # 진입차수가 0이 된 부품 큐에 삽입
            if indegree[part] == 0:
                q.append(part)
                if part not in basic_parts:  # 새로 추가된 부품이 기본 부품이면 추가
                    basic_parts.append(part)

    # 결과 출력
    for i in basic_parts:
        print(i, cnt[i])



# topology_sort()
