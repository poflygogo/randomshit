# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b516. 凱撒密碼-商競103


A = ord('A')
table = [chr((26 + i + 3) % 26 + A) for i in range(26)]
for i in range(int(input())):
    text = input().strip()      # 測資有坑，字串內有非大寫英文字母的字元，務必要 strip() 處理掉
    print(''.join(table[ord(i) - A] for i in text))
