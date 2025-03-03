# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b516. 凱撒密碼-商競103


A = ord('A')
table = {A + i: (i + 3) % 26 + A for i in range(26)}
for i in range(int(input())):
    text = input()
    print(text.translate(table))

# 這是唯一一個不用 strip() 也能 AC 的作法
# 因為這題採取寬鬆比對，允許字串後方有多餘空白字元，而 \r 就屬於空白字元的一份子
# 所以系統在比較答案時，會自動忽略 \r
