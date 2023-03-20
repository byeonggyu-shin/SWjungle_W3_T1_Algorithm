import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# idx==n이되면, 현재값이 최소, 최대인지 검사하고, 재귀를 종료
# https://youtu.be/uNvcqpVEQXY
# https://youtu.be/ok9Pakfkd70

N = int(input())
num = list(map(int, input().split()))
a, b, c, d = map(int, input().split())  # +, -, *, //
max_ans, min_ans = -sys.maxsize - 1, sys.maxsize


def bt(sum, idx, add, sub, mul, div):
    global max_ans, min_ans
    if idx == N:
        max_ans = max(max_ans, sum)
        min_ans = min(min_ans, sum)
        return

    if add > 0:
        bt(sum + num[idx], idx+1, add-1, sub, mul, div)
    if sub > 0:
        bt(sum - num[idx], idx+1, add, sub-1, mul, div)
    if mul > 0:
        bt(sum * num[idx], idx+1, add, sub, mul-1, div)
    if div > 0:
        bt(int(sum / num[idx]), idx+1, add, sub, mul, div-1)


bt(num[0], 1, a, b, c, d)
print(max_ans)
print(min_ans)
