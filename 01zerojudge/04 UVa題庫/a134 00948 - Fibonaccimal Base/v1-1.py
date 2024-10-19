def next_fib():
    global fib, length
    fib.append(fib[-1] + fib[-2])
    length += 1


def fib_base_cac(n: int) -> str:
    temp = []
    while n:
        idx = 0
        while fib[idx] <= n:
            idx += 1
            if idx == length:
                next_fib()
        temp.append(fib[idx - 1])
        n -= fib[idx - 1]
    
    result = ['1']
    for idx in range(1, len(temp)):
        result.extend(['0'] * (fib.index(temp[idx - 1]) - fib.index(temp[idx]) - 1) + ['1'])
    if temp[-1] != 1:
        result.extend(['0'] * fib.index(temp[-1]))
    return ''.join(result)


fib = [1, 2, 3, 5, 8, 13]
length = 6
for _ in range(int(input())):
    dec_base = input()
    print(f'{dec_base} = {fib_base_cac(int(dec_base))} (fib)')


# zerojudge a134
# UVa 00948
# AC (37ms, 3.3MB)
# 2024-10-19
