#구슬찾기 dfs
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

bigger_lst = [[] for _ in range(n+1)]  # index보다 큰 수
smaller_lst = [[] for _ in range(n+1)]  # index보다 작은 수
mid = (n+1)/2  # 개수 기준 중간값 index

for i in range(m):  # 값 입력후 배열
    a, b = map(int, input().split())
    bigger_lst[b].append(a)
    smaller_lst[a].append(b)

def dfs(arr, node): #방문한 깊이 출력
    visited[node]=1
    stack = deque([node,])
    cnt=0
    while stack:
        v = stack.pop()
        for i in arr[v]:
            if visited[i]==0:
                cnt +=1
                visited[i]=1
                stack.append(i)
    return cnt

answer = 0
for i in range(1, n+1):
    visited = [0]*(n+1) #숫자를 1부터 n까지 탐색하면서
    if dfs(bigger_lst, i) >= mid: #중간값보다 확실히 큰값이 있다면 리스트에 저장하고 정답 개수에 추가
        answer += 1
    if dfs(smaller_lst, i) >= mid:
        answer += 1
print(answer)
