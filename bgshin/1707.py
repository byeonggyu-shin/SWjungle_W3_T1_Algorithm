# DFS (중) - 이분 그래프

import sys
from collections import deque
# bfs 함수는 그래프의 정점을 탐색하며 이분 그래프인지 확인하는 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    # bfs 함수 내에서, 현재 정점에서 연결된 정점을 탐색
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if not visited[node]:
                # 아직 방문하지 않은 정점은 현재 정점의 그룹 번호에 -1을 곱한 값을 저장
                visited[node] = -visited[cur]
                # 이전 정점과 다른 그룹 번호가 할당
                queue.append(node)
              # 방문한 정점의 그룹 번호가 현재 정점의 그룹 번호와 같다면, 
              # 이분 그래프 조건을 만족하지 않으므로 False를 반환
            elif visited[node] == visited[cur]:
                return False

    # 만약 탐색을 완료하고도 이런 상황이 발생하지 않았다면, 그래프는 이분 그래프이므로 True를 반환
    return True
#  bipartite_graph 함수는 이분 그래프 문제의 주요 로직을 처리하는 함수
def bipartite_graph(test_case):
    # 테스트 케이스에 대해 그래프를 생성
    for _ in range(test_case):
        V, E = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)
        
        for _ in range(E):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
        
        result = True
        # 방문하지 않은 정점에 대해 bfs를 호출하여 이분 그래프 여부를 확인

        # 모든 정점을 검사하며 bfs 함수를 호출
        for i in range(1, V + 1):
            if not visited[i]:
                if not bfs(graph, i, visited):
                    result = False
                    break
        #  bfs 함수가 False를 반환한다면, 해당 그래프는 이분 그래프가 아니므로 "NO"를 출력
        #  모든 정점에 대해 이분 그래프 조건을 만족한다면 "YES"를 출력
        if result:
            print("YES")
        else:
            print("NO")


test_case = int(sys.stdin.readline())
bipartite_graph(test_case)


