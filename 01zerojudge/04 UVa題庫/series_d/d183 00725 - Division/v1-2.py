# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00725 Division
# ZeroJudge d183


import collections


def main():
    result = division()
    n = int(input())
    while n:
        if n not in result:
            print(f'There are no solutions for {n}.')
        else:
            for i, j in result[n]:
                print(f'{i} / {j:05d} = {n}')   # 除數有可能為 4 位數，前面需要補 0
        n = int(input())


def division(max_value: int=80):
    result = collections.defaultdict(list)

    # 這裡 for 迴圈用了兩個 magic number: 1234 和 49876
    # 1234 代表的是運算式中，除數可能的最小值為 01234 (不可能有更小的了)
    # 49876 則為最大可能的除數，因為開頭如果是 5，一旦乘 2 就會直接超過 1e6，故最大只可能是 49876
    for b in range(1234, 49876 + 1):
        b_set = set(str(b).zfill(5))
        if len(b_set) != 5:
            continue
        
        # 這邊 for 循環如果需要符合題意邏輯的話，應寫成下面的形式:
        # for a in range(b * 2, min(int(1e5), b * max_value + 1), b)
        # 中止條件沒有寫成 min() 是為了效率考量，這麼做可以占用較少的記憶體
        # 記憶體用量大約差 2 倍
        # 不過這樣也能過，算是鑽了點漏洞
        for a in range(b * 2, int(1e5), b):
            a_set = set(str(a))
            if len(a_set) == 5 and not b_set.intersection(a_set):
                result[a // b].append((a, b))

    for i in result:
        result[i].sort()

    return result


if __name__ == '__main__':
    main()
