# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k468. 打靶 (Target)
# 2023-04 TOI 練習賽 新手組

# O(N)


n, s, f = map(int, input().split())
target = map(int, input().split())

cnt = 0
seen = set()
temp_cnt = None

for i in target:
    if i not in seen:
        seen.add(i)
        cnt += 1
    else:
        seen.remove(i)
    
    if i == f:
        s -= 1
        if f in seen:
            temp_cnt = cnt

    if s == 0:
        print(cnt if f in seen else temp_cnt)
        break
