# DFS (중) - 연산자 끼워넣기

import sys
sys.setrecursionlimit(10**6)  

# 연산자의 개수와 숫자 배열을 입력 받습니다.
import sys 

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
opr = list(map(int, sys.stdin.readline().split()))

#  최소값은 양의 무한대로, 최대값은 음의 무한대로 초기화
max_val = -float('inf')
min_val = float('inf')

def dfs(idx, val, add, sub, mul, div):
    global max_val, min_val
    # 현재 인덱스가 숫자 배열의 길이와 같다면
    if idx == n:
        # 결과 값과 최소값 및 최대값을 비교하여 업데이트
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    #  사용 가능한 연산자를 찾아서 연산자를 사용한 후 DFS를 호출
    if add:
        # 호출 시 인덱스와 결과 값을 업데이트 , 해당 연산자의 사용 횟수 -1
        dfs(idx+1, val+lst[idx], add-1, sub, mul, div)
    if sub:
        dfs(idx+1, val-lst[idx], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, val*lst[idx], add, sub, mul-1, div)
    if div:
        if val >= 0:
            dfs(idx+1, val//lst[idx], add, sub, mul, div-1)
        else:
            dfs(idx+1, -((-val)//lst[idx]), add, sub, mul, div-1)
     # DFS 호출이 완료되면 사용 횟수를 다시 원래대로 복구
dfs(1, lst[0], opr[0], opr[1], opr[2], opr[3])
print(max_val)
print(min_val)


