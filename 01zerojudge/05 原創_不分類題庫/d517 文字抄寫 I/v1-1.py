# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d517. 文字抄寫 I

# 這題的 n 可能有 10^5 之多，所以必須用 sys.stdin 讀取，不然容易超時。


from sys import stdin


seen = dict()
for line in stdin:
    cnt = 1
    n = int(line.rstrip())
    for _ in range(n):
        item = next(stdin).rstrip()
        if item not in seen:
            print('New!', cnt)
            seen[item] = cnt
            cnt += 1
        else:
            print('Old!', seen[item])
    seen.clear()
