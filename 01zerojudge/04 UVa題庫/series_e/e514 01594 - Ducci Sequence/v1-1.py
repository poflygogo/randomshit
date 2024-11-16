# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01594 Ducci Sequence
# ZeroJudge e514


for _ in range(int(input())):
    input()     # 陣列長度，對 python 來說不太重要的東西

    array = tuple(map(int, input().split()))
    steps = set()

    while array not in steps:
        steps.add(array)
        array = [abs(array[i] - array[i - 1]) for i in range(len(array))]
        array.append(array.pop(0))
        array = tuple(array)
    
    if all(map(lambda x: x == 0, array)):
        print('ZERO')
    
    else:
        print('LOOP')
