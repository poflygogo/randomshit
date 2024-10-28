for _ in range(int(input())):
    num = int(input())

    factors = {1, num}
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            factors.update({n, num // n})
    factors.remove(num)

    total = sum(factors)
    if num == total:
        print('perfect')
    elif num > total:
        print('deficient')
    else:
        print('abundant')
