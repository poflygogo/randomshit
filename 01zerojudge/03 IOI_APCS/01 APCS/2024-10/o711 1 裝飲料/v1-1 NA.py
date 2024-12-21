# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o711. 1. 裝飲料
# 2024-10 APCS


def main():
    n = int(input())
    cup_info = list(map(int, input().split()))
    liquid = list(map(int, input().split()))
    cup_info[0] **= 2
    cup_info[1] **= 2
    print(fill_drinks(n, cup_info, liquid))


def fill_drinks(n: int, cup_info: list, liquid: list) -> int:
    w, h = cup_info.pop(0), cup_info.pop(1)
    result = []
    for i in range(n):
        rise = liquid[i] // w
        if rise <= h:
            result.append(rise)
            h -= rise
        else:
            rise = h
            liquid[i] -= rise * w
            if cup_info:
                w, h = cup_info
                cup_info.clear()
            else:
                result.append(rise)
                break
            rise_temp = liquid[i] // w
            if rise_temp <= h:
                result.append(rise + rise_temp)
            else:
                result.append(rise + h)
                break
    return max(result)


main()
