# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j179. 資料分類 (Classification)
# 2022-10 TOI 練習賽 新手組


n = input()
while len(n) > 1:
    if len(n) == 4:
        lft, rgt = n[:2].lstrip('0'), n[2:].lstrip('0')
        n = (lft if len(lft) < 2 else str(int(lft[0]) * int(lft[1]))) + (rgt if len(rgt) < 2 else str(int(rgt[0]) * int(rgt[1])))
    elif len(n) == 3:
        n = str(int(n[0]) * int(n[1])).lstrip('0') + str(int(n[1]) * int(n[2]))
    else:
        n = str(int(n[0]) * int(n[1]))
    
    n = n.lstrip('0')

print(n.zfill(1))   # 結果有可能為 0
