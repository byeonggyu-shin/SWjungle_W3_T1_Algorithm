# 트리의 부모 찾기(296ms)
# 다시 풀기, logoo03 참고
import sys, collections
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N+1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

def BFS(node):
    Q = collections.deque([node])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not parent[v]: # if parent[v] == 0 # visited를 parent의 갱신 여부로 파악 가능, visited 리스트 필요없음
                Q.append(v)
                parent[v] = u
BFS(1)
print(*parent[2:], sep='\n') # 간단하게 줄여 출력하기