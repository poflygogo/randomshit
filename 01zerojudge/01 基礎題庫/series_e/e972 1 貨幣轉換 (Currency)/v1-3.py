# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e972. 1. 貨幣轉換 (Currency)
# 2019-05 TOI 練習賽 新手組


def get_ans(money, cost, currency):
    exchange_rate = {
        'T': 1.0,
        'U': 30.9,
        'J': 0.28,
        'E': 34.5
    }
    money /= exchange_rate[currency]
    money -= int(cost)
    if money >= 0:
        if money < 0.05:
            money = 0
        return f'{currency} {money:.2f}'
    else:
        return 'No Money'


def main():
    money = input().rstrip()
    if '\r' in money:
        money, cost, currency = money.replace('\r', ' ').split()
    else:
        cost, currency = input().rstrip().split()
    print(get_ans(int(money), int(cost), currency))


if __name__ == '__main__':
    main()
