import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def post_order(start, end):
    if start > end:
        return

    root = pre_order[start]
    pivot = end + 1
    for i in range(start + 1, end + 1):
        if root < pre_order[i]:
            pivot = i
            break
    post_order(start+1, pivot - 1)
    post_order(pivot, end)
    print(root)

pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break
if pre_order:
    post_order(0, len(pre_order) - 1)
