# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b003. 運算式 + - 符號設定問題
# 95學年度高雄市資訊學科能力競賽


from math import ceil, sqrt


def operate(k: int) -> int:
    k = abs(k)                              # 不在乎正負數
    n = ceil((-1 + sqrt(8 * k + 1)) / 2)    # 用公式解求出 n 至少要有多大才能 >= abs(k)
    temp = (n + 1) * n // 2                 # 等差數列和
    while (temp - k) % 2:                   # 窮舉，若兩數的差不為偶數就 n++
        n += 1
        temp += n
    return n


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        print(operate(n))


if __name__ == '__main__':
    main()
