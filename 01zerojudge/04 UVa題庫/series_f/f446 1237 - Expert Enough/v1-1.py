# -*- encoding: utf-8 -*-
# python 3.12
# UVa 1237 Expert Enough
# ZeroJudge f446



def mainloop():
    # ZeroJudge 的測資第一行有坑，前面多一個空行
    T = input()
    while not T.isdigit():
        T = input()
    T = int(T)
    for _ in range(T):
        factories = []
        for _ in range(int(input())):
            fac, a, b = input().split()
            factories.append((fac, int(a), int(b)))
        for _ in range(int(input())):
            print(get_factory(factories, int(input())))


def get_factory(factories: list, query: int) -> str:
    result = []
    for fac, a, b in factories:
        if a <= query <= b:
            result.append(fac)
        if len(result) > 1:
            return 'UNDETERMINED'
    if result:
        return result[0]
    return 'UNDETERMINED'


mainloop()
