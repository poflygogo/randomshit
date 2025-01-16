# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k570. pA. 關於友善時光這件事


def discount(id, hour, minute, price):
    minute_total = hour * 60 + minute
    if minute_total == 0:
        minute_total = 1440
    if id == 0 and 1080 <= minute_total <= 1440:
        return price * 7 // 10
    elif id == 1 and 600 <= minute_total <= 1440:
        return price * 7 // 10
    elif id == 2 and (600 <= minute_total <= 1020 or 1200 <= minute_total <= 1440):
        return price * 65 // 100
    elif id == 3 and 990 <= minute_total <= 1350:
        return price * 6 // 10
    return price


def main():
    print(sum(
        discount(*map(int, input().split()))
        for _ in range(int(input()))
    ))


if __name__ == "__main__":
    main()
