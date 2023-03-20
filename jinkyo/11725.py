"""
트리의 부모 찾기
input으로 edges만 들어옴.
root node(1)을 줌으로써 edges들의 연결을 탐색해 부모를 출력해야 한다.
부모를 담을 table을 만들자.
--> 방법: dfs로 부모-자식간으로 들어가면서 부모table에 저장하자.
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

#방향성을 모르는 edges로 들어왔으니 adjacency list로 변환
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)

log = [0]*(n+1) #

def dfs(node=1):
    visited[node]= True #현재탐색 노드를 방문처리하고

    for i in graph[node]:  # 현재탐색 노드와 연결된 노드들을 돌면서
        if not visited[i]: #연결된 노드가 방문되지 않은 노드라면, 재귀(똑같은 함수 호출)
            dfs(i)
        log[i] = node
dfs()
for i in log[2:]:
    print(i)
