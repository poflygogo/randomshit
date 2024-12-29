# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b119. 售票系統 (Sales)
# 95 學年度台北市資訊學科能力競賽


def main():
    while True:
        try:
            data = list(map(int, input().split()))
        except:
            break
        print(plane_sale_system(data.pop(0), data.pop(0), data.pop(0), data))


def plane_sale_system(s, t, n, iterable):
    """
    args:
        s       : int, 該航班的票面價
        t       : int, 機位數
        n       : int, 訂位紀錄總數, 相當於 len(iterable)
        iterable: list[int], 每個訂位的機位數
    return:
        int, 利潤
    """
    standard = t // 5
    total_book = sum(iterable)
    income = 0
    for i in range(3):
        if total_book <= 0:
            break
        income += (total_book if total_book < standard else standard) * s * (0.7, 0.8, 0.9)[i]
        total_book -= standard
    if total_book > 0:
        income += 2000 * total_book
    return round(income - s * t * 0.3) 


if __name__ == '__main__':
    main()
