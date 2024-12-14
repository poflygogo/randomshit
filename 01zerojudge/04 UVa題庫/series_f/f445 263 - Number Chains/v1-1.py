# -*- encoding: utf-8 -*-
# python 3.12
# UVa 263 Number Chains
# ZeroJudge f445


def mainloop():
    from sys import stdin

    for num in stdin:
        num = int(num.rstrip())
        if num == 0:
            break
        print(f'Original number was {num}')

        seen = set()
        while num not in seen:
            seen.add(num)
            a = ''.join(sorted(list(str(num))))
            b = int(a[::-1])
            a = int(a)
            b = int(b)
            num = b - a
            print(f'{b} - {a} = {num}')
        print(f'Chain length {len(seen)}', end='\n\n')


mainloop()
