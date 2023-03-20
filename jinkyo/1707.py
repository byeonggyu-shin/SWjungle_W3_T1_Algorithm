"""
이분그래프
:노드끼리 서로 인접하지 않는 두 집합으로 그래프 노드를 나눌 수 있는 그래프
dfs문제
"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

k = int(input())


def dfs(node, visited):
    visited[node] = True
    for i in adj_list[node]: #연결된 노드의 목록을 탐색하는데
        if not visited[i] : #방문처리 되지 않은 노드라면
            grouping[i] = (grouping[node] +1)%2  # 현재 탐색노드를 그룹1로 지정
            dfs(i, visited)  # 그 노드에 대해 똑같은 함수 호출
        # 이미 방문한 노드인데 현재 나의 노드와 같은 집합이면 이분그래프가 아님
        else:
            if grouping[i] == grouping[node]:
                return False
    else:
        return True

for _ in range(k):
    n, v = map(int, input().split())
    adj_list = [[] for i in range(n+1)]  # [[], [2], [1, 3, 4], [2, 4], [3, 2]]
    visited = [False]*(n+1)
    grouping = [False]*(n+1) 
    result = []
    for _ in range(v):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    for i in range(1, n+1):
        result.append(dfs(i, visited))
    if False in result:
        print('NO')
    else:
        print('YES')