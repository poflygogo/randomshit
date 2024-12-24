# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q027. 喵-17的倍數

# 數字相當巨大，直接轉換成 int 不理智 n <= 2^(2^20)
# 這邊使用 17 的整除規則，由右至左，每 8 位數字就切割一次
# 然後將得到的一系列的 8 位數交替加減，檢視最後結果是否能被 17 整除

# 取模時不直接使用該數字 % 17
# 而是利用模運算的特性
# (ab + c) % m = ((a % m)(b % m) + c % m) % m


def main():
    num         = input()
    length      = len(num)
    reminder    = length % 17
    split_point = reminder if reminder != 0 else 8
    num_split   = [int(num[:split_point])]
    num_split.extend([int(num[i:i + 8]) for i in range(split_point, length, 8)])
    num_split.reverse()
    check       = sum(n if i % 2 == 0 else -n for i, n in enumerate(num_split))
    if check % 17 == 0:
        print('Yes')
    else:
        mod = 0
        for digit in num:
            mod = (mod * 10 + int(digit)) % 17
        if mod >= 9:
            mod = 17 - mod
        print(mod)


if __name__ == '__main__':
    main()
