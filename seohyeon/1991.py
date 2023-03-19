# 트리 순회
# cih831 코드 참고, 가독성 향상
import sys
input = sys.stdin.readline

def preorder(key):
    if key == '.':
        return
    print(key, end='')
    preorder(tree[key][0])
    preorder(tree[key][1])

def inorder(key):
    if key == '.':
        return
    inorder(tree[key][0])
    print(key, end='')
    inorder(tree[key][1])

def postorder(key):
    if key == '.':
        return
    postorder(tree[key][0])
    postorder(tree[key][1])
    print(key, end='')

tree = {} # 딕셔너리
for _ in range(int(input())):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')