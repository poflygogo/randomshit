"""
位運算
只有當 m 為偶數時才有用
"""

# from sys import stdin
stdin = open(r'01zerojudge\06 未解之謎\d578 小涵的積木\test file\test.txt')


for line in stdin:
    n, m = map(int, line.strip().split())
    if n == m == 0: break

    length = n * m - 1
    data = {}
    r = 0
    for _ in range(length):
        item = next(stdin).strip()
        ascll = sum(ord(i) for i in item)
        data[ascll] = item
        r ^= ascll
    
    print(data[r])
