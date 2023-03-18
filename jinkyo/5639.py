"""
이진검색트리 
이진검색트리 구현 문제, 전위순환으로 input된 데이터를 후위순환으로 출력하는 문제
이진검색트리란? 탐색 효율을 높이도록 고안된 트리구조, 왼쪽자식노드 < 부모노드 < 오른쪽 자식 노드

전위 순환이었으니까 각 서브트리의 루트보다 큰 값이 나오면 그게 오른쪽 자식=오른쪽 서브트리의 루트가 된다. (그 전까지는 다 왼쪽 자식이 루트인 트리)
값을 다 받아 저장한 다음, 자식이 더 없을 때까지 가장 작은 트리로 나눠가기, 인덱스 활용"
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

#전위순회값의 ><=의 데이터를 이용하지 않고, 루트노드로 다시 후위순회 구성
def post_order(start, end): #strat, end의 index값을 줌
    if start > end: #탐색index가 끝보다 커지면, 즉 탐색범위를 다 순회하면 종료
        return

    root = pre_order[start] #입력의 처음값이 루트노드-기준점
    pivot = end + 1 #초기설정값은 전체를 탐색할 수 있도록 초기화
    for i in range(start+1, end+1): #루트노드의 다음 입력부터, 데이터의 끝까지 순회하면서
        if root < pre_order[i]: #탐색값이 root보다 크다면
            pivot = i #pivot에 해당 인덱스 저장
            break #종료
    post_order(start+1, pivot - 1) #pivot(루트노드보다 큰 입력)을 기준으로 왼쪽서브트리 재귀호출
    post_order(pivot, end)  # pivot(루트노드보다 큰 입력)을 기준으로 오른쪽서브트리 재귀호출
    print(root) #결국엔 루트가 되어야 출력한다. 그러기 위해 재귀함수 호출


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break
if pre_order:
    post_order(0, len(pre_order) - 1)
