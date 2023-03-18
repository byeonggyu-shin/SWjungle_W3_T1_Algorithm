"""
트리 순회 
전위순회, 중위순회 ,후위순회를 구현하는 방법 연습
input
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

input이 다음과 같이 root, 왼쪽자식, 오른쪽 자식으로 주어졌을 때,
dict를 이용해서 tree를 구성하고 원하는 순서에 따라 값 출력

output
ABDCEFG
DBAECFG
DBEGFCA

"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input().strip())
tree={}

for n in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def pre_order(root):
    if root != '.': #루트노드가 있다면
        print(root, end='') # 자신을 먼저 출력하고
        pre_order(tree[root][0]) #left 방문하고
        pre_order(tree[root][1])  # right 방문

def in_order(root):
    if root != '.': #루트노드가 있다면
        in_order(tree[root][0])  # 왼쪽노드 먼저 방문하고
        print(root, end='')  # 자신 방문하고
        in_order(tree[root][1])  # 오른쪽 방문하고


def post_order(root):
    if root != '.': #루트노드가 있다면
        post_order(tree[root][0])  # 왼쪽 방문하고
        post_order(tree[root][1])  # 오른쪽 방문하고
        print(root, end='')  # 루트 자신을 방문하고

pre_order('A')
print()
in_order('A')
print()
post_order('A')
