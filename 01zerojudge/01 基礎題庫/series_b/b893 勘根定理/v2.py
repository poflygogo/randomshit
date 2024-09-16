from sys import stdin, stdout

def zi_func(n:int) -> int:
    return (a * n ** 5) + (b * n ** 4) + (c * n ** 3) + (d * n ** 2) + (e * n) + f

a, b, c, d, e, f = map(int, stdin.readline().strip().split())

if a == b == c == d == e == 0:
    if f:
        stdout.write(r'N0THING! >\\<')
    else:
        stdout.write('Too many... = ="')
else:
    result = []
    for i, j in zip(range(-35, 35), range(-34, 36)):
        func_i = zi_func(i)
        func_j = zi_func(j)
        if func_i * func_j < 0:
            result.append(f'{i} {j}')

        elif func_i * func_j == 0:
            if func_i == 0:
                result.append(f'{i} {i}')

    if result:
        result = '\n'.join(result)
        stdout.write(result)
    else:
        stdout.write(r'N0THING! >\\<')