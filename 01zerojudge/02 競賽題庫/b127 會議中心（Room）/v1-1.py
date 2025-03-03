# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b127. 會議中心（Room）


from functools import lru_cache


@lru_cache(None)
def room(n: int):
    if n <= 2:
        return n
    return room(n - 1) + room(n - 2)


while True:
    try:
        print(room(int(input())))
    except EOFError:
        break
