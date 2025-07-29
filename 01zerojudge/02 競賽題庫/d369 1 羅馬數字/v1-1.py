# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d369. 1. 羅馬數字
# 96學年度全國資訊學科能力競賽


to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def rome_to_int(s: str) -> int:
    if s == "":
        return 0
    result = to_int[s[0]]
    for i in range(1, len(s)):
        result += to_int[s[i]]
        if to_int[s[i]] > to_int[s[i - 1]]:
            result -= to_int[s[i - 1]] * 2
    return result


to_rome = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def int_to_rome(n: int) -> str:
    result = []
    for i in to_rome:
        while n >= i:
            result.append(to_rome[i])
            n -= i
    return "".join(result)


def main():
    for _ in range(int(input())):
        a, b = input().split()
        if a == "1":
            print(rome_to_int(b))
        else:
            print(int_to_rome(int(b)))


main()
