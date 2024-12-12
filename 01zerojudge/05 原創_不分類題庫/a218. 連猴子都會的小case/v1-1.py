# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a218. 連猴子都會的小case


def mainloop():
    while True:
        try:
            input()
        except EOFError:
            break
        else:
            print(sorted_nondupe_number(input().split()))
    

def sorted_nondupe_number(data: list) -> str:
    counter = {}
    for i in data:
        counter[i] = counter.get(i, 0) + 1
    return ' '.join(sorted(counter, key=lambda x: (-counter[x], int(x))))


mainloop()
