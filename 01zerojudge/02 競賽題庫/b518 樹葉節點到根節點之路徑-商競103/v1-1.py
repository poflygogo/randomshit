# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b518. 樹葉節點到根節點之路徑-商競103
# 103學年度商業類程式設計競賽模擬題

# ---------------------------------------------------

import sys
import io
Q = """
3
7
0,99
1,3
2,3
3,5
4,6
5,0
6,5
4
0,99
1,0
2,0
3,0
1
0,99
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



def main():
    for test_case in range(int(input())):
        if test_case > 0:
            print()
        n = int(input())
        data = list(range(n))
        for _ in range(n):
            a, b = map(int, input().split(","))
            data[a] = b

        for i in set(range(n)) - set(data):
            t = data[i]
            result = []
            while t < len(data) and data[t] != 99:
                result.append(t)
                t = data[t]
            if result:
                print(f'{i}:{{{formatter(result)}}}')
            else:
                print(f'{i}:N')


def formatter(arr: list):
    # 只是想讓輸出好看一點 :(
    # 不然寫一堆引號太瘋了
    return ','.join(map(str, arr))


main()
