# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11063 B2-Sequence
# ZeroJudge d123


cases = 0
while True:
    try:
        length = int(input())
    except EOFError:
        break
    else:
        cases += 1
        data = tuple(map(int, input().split()))

        # 列出不符合的條件，依序為:
        # 1) 首項數字小於 1
        # 2) b_{i} >= b_{j}(i < j)
        # 3) 不重複的元素總數 != 理論上應該要有的元素總數
        if data[0] < 1 or \
            any(data[i] >= data[i + 1] for i in range(length - 1)) or \
            len({data[i] + data[j] for i in range(length) for j in range(i, length)}) != length * (length - 1) // 2 + length:
            flag = False
        
        else:
            flag = True
        
        print(f'Case #{cases}: It is {"" if flag else "not "}a B2-Sequence.')
