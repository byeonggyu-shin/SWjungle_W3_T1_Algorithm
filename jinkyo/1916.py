#최소비용 구하기
#다익스트라
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split()) # a는 출발도시번호, b는 도착지의 도시번호, c는 버스 비용
    graph[a].append((b,c))

x, y = map(int, input().split())
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)
print(distance[y])