# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q868. 題目推薦


# ---------------------------------------------------

import sys
import io
Q = """5
1 2
2 3
3 4
4 5
5 6
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

def is_connected(s: int, e: int) -> bool:
    if s == e:
        return True
    for i in data.get(s, set()):
        return is_connected(i, e)
    return False
    

print("Yay" if is_connected(*map(int, input().split())) else "Come on")
