# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k468. 打靶 (Target)
# 2023-04 TOI 練習賽 新手組

# TOFIX: 當第 s 個 f 是被老闆打爆時會輸出錯誤結果


n, s, f = map(int, input().split())
target = map(int, input().split())

cnt = 0
seen = set()

for i in target:
    s -= (i == f)
    if i not in seen:
        seen.add(i)
        cnt += 1
    else:
        seen.remove(i)
    
    if s == 0:
        print(cnt)
        break
