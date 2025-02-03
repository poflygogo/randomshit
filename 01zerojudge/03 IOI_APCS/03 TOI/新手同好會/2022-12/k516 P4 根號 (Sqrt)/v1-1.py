# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k516. P4.根號 (Sqrt)
# 2022-12 TOI 新手同好會

# 連自己都看不懂的程式碼系列，我到底在寫什麼


n = int(input())

a = n * 2
b = n // 2
c = (n & 1 == 0)

abc = a + b - c - 2
gap = abc - n - b

for row in range(n):
    if row == 0:
        print(' ' * abc + '*' * a)
    
    elif row < b:
        print(' ' * (abc - row) + '*')

    elif row == b:
        print('*' * n + ' ' * gap + '*')
    
    elif row == n - 1:
        print(' ' * (n + b - 1 - c) + '*')
    
    else:
        print(' ' * (n + row - b - 1) + '*' + ' ' * (gap - 2 * (row - b)) + '*')
