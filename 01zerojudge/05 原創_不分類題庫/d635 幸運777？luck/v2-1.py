from sys import stdin


for n in stdin:
    n = int(n.rstrip())
    if n < 0:
        print('-1')
        break

    result = []
    while n >= 8:
        result.append(n % 8)
        n //= 8
    result.append(n)

    print(
        *reversed(result),
        sep=''
    )
