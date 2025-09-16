# ZeroJudge b976. 5.最終任務->a.尋找提示
# https://zerojudge.tw/ShowProblem?problemid=b976


# ---------------------------------------------------

import sys
import io
Q = """
3 1
3 2
3 3
3 2
3 2
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


def distance(info):
    id, locate = info
    return (locate[0] - x)**2 + (locate[1] - y)**2, id


n, m = map(int, input().split())
data = [(i, tuple(map(int, input().split()))) for i in range(1, n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    print(min(data, key=distance)[0])
