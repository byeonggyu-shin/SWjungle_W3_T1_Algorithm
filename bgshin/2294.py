#  BFS (상) - 동전 2

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

# 큐에 담는다 
# 가장 큰수 부터 많이 사용하도록 

def bfs(coins, k):
    # k까지 가는 방법으로 생각
    visited = [False] * (k + 1)

    q = deque([0])
    # 0번째(가장 큰 코인) 사용
    visited[0] = True
    cnt = 0
    # 사용할 코인 종류가 남았다면
    while q:
        size = len(q)
        for _ in range(size):
            current = q.popleft()
            # k값이 되었다면 next해본 횟수 cnt 리턴
            if current == k:
                return cnt
            # ?
            for coin in coins:
              # 현재 값에 모든 종류 한번씩 더해보고
                next_value = current + coin
                # 만약 더한값이 유효값사이고 이 값까지 온적이 없다면
                if 0 <= next_value <= k and not visited[next_value]:
                    visited[next_value] = True
                    # 이 값도 큐에 넣어서 돌려보자
                    q.append(next_value)
        cnt += 1

    return -1

# 코인 유효성 검사 필요는 없는듯
# for _ in range(n):
#     coin = int(sys.stdin.readline())
#     if coin <= k:
#         coins.append(coin)

print(bfs(coins, k))