# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a251. 假費波那契數


def mainloop():
    for _ in range(int(input())):
        print(fake_fib(*map(int, input().split())))


def fake_fib(ask, *args):
    if len(args) == ask:
        return sorted(args)[ask // 2]
    return fake_fib(ask, *args, args[-1] + args[-4])


mainloop()
