# 그래프 탐색 기본 (하) - 트리 순회

import sys

class Node:
  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

#  전위 순회
def preorder(node):
  print(node.item, end="")
  if node.left != '.':
    preorder(tree[node.left])
  if node.right != '.':
    preorder(tree[node.right])
#  중위 순회
def inorder(node):
  if node.left != '.':
    inorder(tree[node.left])
  print(node.item, end="")
  if node.right != '.':
    inorder(tree[node.right])
#  후위 순회
def postorder(node):
  if node.left != '.':
    postorder(tree[node.left])
  if node.right != '.':
    postorder(tree[node.right])
  print(node.item, end="")

n =int(sys.stdin.readline())
tree = {}

for _ in range(n):
  node, left, right = map(str, input().split())
  tree[node] = Node(item=node, left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])