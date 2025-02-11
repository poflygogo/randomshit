# -*- encoding: utf-8 -*-
# python 3.12
# NOIP 2009


def poly(max_exponent, data):
    data = list(reversed(data))
    result = [
        f'{"" if data[i] == 1 and i != 0 else "-" if data[i] == -1 and i != 0 else data[i]}'
        f'{"" if i == 0 else "x"}'
        f'{"" if i in (0, 1) else f"^{i}"}'
        for i in range(max_exponent + 1)
        if data[i] != 0
    ]
    result = '+'.join(reversed(result)).replace('+-', '-')
    return result if result else '0'


def main():
    length = int(input())
    data = list(map(int, input().split()))
    print(poly(length, data))


main()
