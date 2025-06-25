# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q868. 題目推薦


# ---------------------------------------------------

import sys
import io
Q = """4
1 2
3 4
5 6
1 7
1 6"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------

data: dict[int, set[int]]

data = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a not in data:
        data[a] = {b}
    else:
        data[a].add(b)

def is_connected(s: int, e: int, path: set) -> bool:
    if s == e:
        return True
    if s not in data or s in path:
        return False
    path.add(s)
    return is_connected(data[s], e, path)

print("Yay" if is_connected(*map(int, input().split()), path=set()) else "Come on")
