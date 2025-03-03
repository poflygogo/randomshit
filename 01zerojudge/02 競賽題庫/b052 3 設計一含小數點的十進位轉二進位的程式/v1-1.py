# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b052. 3. 設計一含小數點的十進位轉二進位的程式
# 96學年度高雄市資訊學科能力競賽


while True:
    try:
        integer, decimal = input().split('.')
    except EOFError:
        break

    integer_bin = bin(int(integer))[2:]
    decimal_bin = ''
    decimal = float('0.' + decimal)
    while decimal:
        decimal *= 2
        a, decimal = divmod(decimal, 1)
        decimal_bin += str(int(a))
    print(integer_bin + '.' + decimal_bin)
