#  DFS (상) - 구슬 찾기

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

# 주어진 입력에 대해 두 개의 그래프를 생성합니다. 
# 하나는 무거운 구슬의 관계를 나타내고, 
heavier = defaultdict(list)
# 다른 하나는 가벼운 구슬의 관계를 나타냅니다.
lighter = defaultdict(list)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    heavier[y].append(x)
    lighter[x].append(y)
# 이때, 무거운 구슬 그래프에서 DFS를 사용하여 무거운 구슬의 수를 구하고, 
# 가벼운 구슬 그래프에서 DFS를 사용하여 가벼운 구슬의 수를 구합니다.
def dfs(graph, visited, start):
    count = 0
    stack = [start]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            count += 1
            stack.extend(graph[current])
    return count

result = 0
mid = (n + 1) // 2

for i in range(1, n + 1):
    heavy_visited = [False] * (n + 1)
    light_visited = [False] * (n + 1)
    # 각 구슬에 대해 DFS를 사용하여 무거운 구슬의 수와 가벼운 구슬의 수를 구합니다.

# 중간 구슬보다 무거운 구슬의 수가 (N + 1) // 2 개 이상이거나, 
# 중간 구슬보다 가벼운 구슬의 수가 (N + 1) // 2 개 이상인 구슬을 찾습니다.
    if dfs(heavier, heavy_visited, i) > mid or dfs(lighter, light_visited, i) > mid:
        result += 1

# 해당 조건을 만족하는 구슬의 개수를 출력합니다.
print(result)
