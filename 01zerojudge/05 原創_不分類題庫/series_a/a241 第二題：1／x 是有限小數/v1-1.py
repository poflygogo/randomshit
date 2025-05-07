#  -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a241. 第二題：1 / x 是有限小數


def mainloop():
    for _ in range(int(input())):
        print(len([True for i in range(1, int(input()) + 1) if is_valid(i)]))


def is_valid(n: int) -> bool:
    if int(str(n)[-1]) not in (0, 2, 4, 5, 6, 8):
        return False
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    if n == 1:
        return True
    return False


mainloop()
