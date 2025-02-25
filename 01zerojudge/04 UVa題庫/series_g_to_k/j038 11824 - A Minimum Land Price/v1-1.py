# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11824 A Minimum Land Price
# ZeroJudge j038


limit = int(5e6)
for _ in range(int(input())):
    arr = [int(input())]
    while arr[-1] != 0:
        arr.append(int(input()))
    
    arr.pop()
    arr.sort(reverse=True)

    total = 0
    for i in range(len(arr)):
        total += 2 * arr[i] ** (i + 1)
        if total > limit:
            print('Too expensive')
            break
    else:
        print(total)
