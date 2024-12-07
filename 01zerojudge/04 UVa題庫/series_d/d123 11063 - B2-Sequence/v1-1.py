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

        # 若首項數字小於 1 或 b_{i} >0 b_{j}(i < j)，則必定不是 B2 數列 
        if data[0] < 1 or \
            any(data[i] >= data[i + 1] for i in range(length - 1)) or \
            len({data[i] + data[j] for i in range(length) for j in range(i, length)}) != length * (length - 1) // 2 + length:
            flag = False
        
        else:
            flag = True
        
        print(f'Case #{cases}: It is {"" if flag else "not "}a B2-Sequence.')
