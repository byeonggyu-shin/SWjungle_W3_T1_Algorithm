# DFS (중) - 아침 산책

import sys
sys.setrecursionlimit(10**6)  

n = int(sys.stdin.readline())
a = str(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node ,visited):
    
    global cnt
    # 방문 노드 기록
    visited[node] = True
   
    for child in graph[node]:    
        # 방문한 노드라면 통과
        if visited[child]:
            continue
    
        node = child
        # 거치는 곳이 외부 (0) 이라면 dfs 실행
        if a[node-1]=='0':
            dfs(node,visited)
        #  거치는 곳이 실내라면 (1) cnt 해주고 탈출
        else:
            cnt += 1
    return    
   
cnt = 0

for i in range(1,n+1):
    # 건물일 때만 산책 시작 
    if a[i-1] != '0':
        #  방문 기록 초기화
        visited = [False] * (n+1)
        dfs(i, visited)
print(cnt)