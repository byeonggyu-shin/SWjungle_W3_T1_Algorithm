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
