# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k851. P5.辨識碼 (Identification)
# 2021-10 TOI 新手同好會


def identify(s: int, sep: int=3) -> bool:
    seen = set()
    while s > 0:
        temp = 0
        for _ in range(sep):
            s, mod = divmod(s, 10)
            temp += mod
            if s <= 0:
                break
        if temp in seen:
            return True
        seen.add(temp)
    return False


if __name__ == '__main__':
    x = int(input())
    n = int(input())
    print('Yes' if identify(n, x) else 'No')
