def n_and_m(depth, n, m):

  if depth == m:
    print(' '.join(map(str, answer)))

  for i in range(1, n+1):

    if not visited[i]:
      visited[i] = True
      answer.append(i)
      n_and_m(depth+1, n, m)
      visited[i] = False
      answer.pop()


n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []

n_and_m(0, n, m)
