# # DFS (중) - 아침 산책

# import sys
# sys.setrecursionlimit(10**6)  

# n = int(sys.stdin.readline())
# a = str(sys.stdin.readline())

# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     u,v = map(int, sys.stdin.readline().split())
#     graph[u].append(v)
#     graph[v].append(u)

# def dfs(node ,visited):
    
#     global cnt
#     # 방문 노드 기록
#     visited[node] = True
    
#     for child in graph[node]:    
#         # 방문한 노드라면 통과
#         if visited[child]:
#             continue
    
#         node = child
#         # 거치는 곳이 외부 (0) 이라면 dfs 실행
#         if a[node-1]=='0':
#             dfs(node,visited)
#         #  거치는 곳이 실내라면 (1) cnt 해주고 탈출
#         else:
#             cnt += 1
#     return    
   
# cnt = 0

# for i in range(1,n+1):
#     # 건물일 때만 산책 시작 
#     if a[i-1] != '0':
#         #  방문 기록 초기화
#         visited = [False] * (n+1)
#         dfs(i, visited)
# print(cnt)



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def calPaths(graph: list, col: list) -> int:
    count = 0
    visited = set()

    def dfs(exterior: int) -> int:
        cnt = 0
        for neighbor in graph[exterior]:
            if col[neighbor] == 1:
                cnt += 1
            else:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cnt += dfs(neighbor)
        return cnt

    for i in range(1, numVertices + 1):
        # 각 실내별 인접한 실내 구하기
        if col[i] == 1:
            for j in graph[i]:
                if col[j] == 1:
                    count += 1
        # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤 
        # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp - 1)
 
    return count


numVertices = int(input())
col = list(map(int, list("0"+input().strip())))

graph = [[] for _ in range(numVertices + 1)]

for _ in range(1, numVertices):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(calPaths(graph, col))