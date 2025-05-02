# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10041 Vito's family
# ZeroJudge a737


for _ in range(int(input())):
    r, *data = map(int, input().split())
    data.sort()

    # find median
    if r % 2:
        home = data[r // 2]
    else:
        home = (data[r // 2 - 1] + data[r // 2]) / 2
    
    result = sum(abs(home - i) for i in data)
    print(int(result))
