"""
아침산책
dfs
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input()) #정점의 수

#실내외 데이터 table indoor_check
indoor_check = [0]*(n+1)  # 실내는 1, 실외는 0 [0, 1, 0, 1, 1, 1]
data = str(input()) 
for i in range(1, n+1):
    indoor_check[i] = int(data[i-1])

#tree table, 무방향
adj_list = [[] for _ in range(n+1)]  # [[], [2], [1, 3, 4], [2], [2, 5], [4]]
for _ in range(n-1): #간선의 개수만큼
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

#산책경로 세는 변수
count = 0
#루트노드를 함수 input으로
def dfs(node):
    global count
    visited[node] = 1  # 루트노드 방문처리
    for i in adj_list[node]: #연결된 노드들을 탐색하는데
        if visited[i] == 0 and indoor_check[i] == 1:  # 방문하지 않은 장소인데, 실내면 count하고
            visited[i]==1
            count +=1
            continue
        elif visited[i] == 0 and indoor_check[i] == 0:  # 방문하지 않은 장소인데, 실외이고,
            dfs(i) 


for i in range(1,n+1): #노드의 개수만큼, i는 탐색노드
    if indoor_check[i]==1: #시작이 실내인 것만 dfs로 탐색
        visited = [0]*(n+1)  # 방문 table, 각 노드를 돌때마다 초기화
        dfs(i)

print(count)


"""문제 풀이 논리
1. 실외 점을 기준으로 인접해있는 실내 노드 개수를 count한다.
2. 실외 점을 중간에 놓고 실내 점 n개가 붙어있을 때 갈 수 있는 경로의 수는 n * 1(중간 실외 점 선택) * (n-1) = n*(n-1)에 해당.
3. 실외 노드끼리 연결되는 경우는 1) 실외끼리 인접 노드로 연결될 때 2) 중간에 실내 노드를 끼고 연결할 때. 이를 분리해서 생각.
"""

n = int(input())  # 정점 수 받기

# location : 실내외 정보 table
location = [0]+list(map(int, input().strip()))

graph = [[] for _ in range(n+1)]  # edges에 대한 정보를 담을 table 초기화

ans = 0 #output값으로 보낼 산책코스 개수를 담을 변수
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b) # 무방향 트리
    graph[b].append(a)  # 무방향 트리
    if location[a] == 1 and location[b] == 1:  # 둘다 실내이면
        ans += 2  # 서로 방문하는 케이스가 2가지이니 이걸 정답에 함께 바로 세는 걸로.

def dfs(v, cnt):  # v: 시작 실외노드 & cnt: 실외와 연결된 실내 노드 개수를 셀 변수cnt
    visited[v] = True # 노드 방문처리

    for i in graph[v]:  # 노드 v와 연결된 인접 노드를 하나씩 불러온다.
        if location[i] == 1:  # 해당 노드의 위치가 실내이면
            cnt += 1  # 실내 개수 카운트에 +1을 해준다
        elif not visited[i] and location[i] == 0:  # 방문하지 않고 해당 i 점의 위치가 실외이면
            cnt = dfs(i, cnt)  # 해당 실외 점을 기준으로 dfs를 돈다!
    return cnt

sum = 0 #수학적 접근 n(n+1)을 통해 연산 효율을 높여 계산한 결과값들.
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i] and location[i] == 0:  # 실외인 애들을 기준으로
        x = dfs(i, 0)  # 현재 cnt = 0
        # 실외인 노드를 기준으로 인접 노드 애들 개수 세는 게 총 n*(n-1)이니 실외 노드 걸릴 때마다 이걸 전부 세기
        sum += x*(x-1)

print(sum + ans)