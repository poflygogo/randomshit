# ZeroJudge b977. 6.最終任務->b.交換提示
# https://zerojudge.tw/ShowProblem?problemid=b977


n, m, q = map(int, input().split())
data = [set(map(int, input().split()[1:])) for _ in range(n)]
for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(len(data[a] - data[b]) * len(data[b] - data[a]))
