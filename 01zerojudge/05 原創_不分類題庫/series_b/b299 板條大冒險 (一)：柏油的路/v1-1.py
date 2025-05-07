# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b299. 板條大冒險 (一)：柏油的路


def mainloop():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(
            'YEEES!!! INKER!' if n <= min(map(int, input().split())) else
            'NOOOO!!! JACKY XX!'
        )


mainloop()
