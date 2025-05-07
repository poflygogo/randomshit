# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a699. 1、国王的烦恼(King)


def mainloop():
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        else:
            print(
                "It's a prime!!!" if is_prime(n) else
                "It's not a prime!!!"
            )


def is_prime(n: int) -> bool:
    """試除法"""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if any(n % i == 0 for i in (2, 3)):
        return False
    if any(n % i == 0 or n % (i + 2) == 0 for i in range(5, int(n ** 0.5) + 1)):
        return False
    return True


mainloop()
