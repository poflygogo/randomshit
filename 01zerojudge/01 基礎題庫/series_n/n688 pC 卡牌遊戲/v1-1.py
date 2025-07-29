# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n688. pC. 卡牌遊戲

# 取得 N, K
N, K = [int(i) for i in input().split()]

# 取得 N 個數字並排序
a = sorted([int(i) for i in input().split()])

# 將負數與正數分開
am = [] # 負數
ap = [] # 正數
for number in a:
    if number < 0:
        am.append(number)
    else:
        ap.append(number)

# 計算負數的數量
am_length = len(am)

# 如果 K 小於等於負數的數量
if K <= am_length:
    for i in range(K): # 將前 K 個負數轉為正數
        am[i] = -am[i]
    ans = sum(am) + sum(ap) # 狀況 1.

# 如果 K 大於負數的數量
else:
    # 如果 K 減去負數的數量後是偶數
    # 則將所有負數轉為正數
    # 剩下的次數可兩兩抵銷
    if (K - am_length) % 2 == 0:
        ans = - sum(am) + sum(ap) # 狀況 2.、狀況 4.

    # 如果 K 減去負數的數量後是奇數
    # 且負數的數量不為 0
    # 必須從已經轉換的負數或正數中選擇一個數字轉為負數
    elif am_length:
        # 最大負數轉正後比最小正數小
        # 將最大負數轉正後再轉為負數最划算
        if -am[-1] < ap[0]:
            ans = -sum(am[:-1]) + am[-1] + sum(ap) # 狀況 3-1.

        # 最大負數轉正後比最小正數大
        # 將最小正數轉為負數最划算
        else:
            ans = -sum(am) + sum(ap[1:]) - ap[0] # 狀況 3-2.

    # 沒有負數，且 K 為奇數，則取最小正數轉為負數
    else:
        ans = sum(ap[1:]) - ap[0] # 狀況 5.

print(ans)