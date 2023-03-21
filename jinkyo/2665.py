# #미로만들기 
# #다익스트라
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n=int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
#여기까지가 input 받기

map = [[None]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]==0: #검은색이면,
            map[i][j] = (1,(i,j))
        else:
            map[i][j] = (0,(i,j))
# print(map)
#사용 변수
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
dx = [1,0,-1,0] #우하좌상
dy = [0,1,0,-1]
distance = [[INF]*n for _ in range(n)] #최단 거리 테이블 모두 무한으로 초기화

def dijkstra(x,y):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, map[0][0]) # (0, (0, 0))
    distance[x][y]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + map[nx][ny][0]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost,(nx,ny)))


dijkstra(0,0)
print(distance[n-1][n-1])