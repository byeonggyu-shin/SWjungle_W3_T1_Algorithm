# 그래프 탐색 기본 (하) - 이진 검색 트리

import sys
sys.setrecursionlimit(10**6)  

lst = []

while True:
    try:
        lst.append(int(sys.stdin.readline()))
    except:  # 입력이 끝나면 종료합니다.
        break


def postorder_traversal(first, end):
    if first > end:
        return
    mid = end+1  # 루트보다 큰 값이 존재하지 않을 경우를 대비   
    for i in range(first+1 , end+1):
        if lst[first] < lst[i]:
            mid = i
            break

    postorder_traversal(first+1, mid-1)
    postorder_traversal(mid, end)
    print(lst[first])

postorder_traversal(0, len(lst)-1)