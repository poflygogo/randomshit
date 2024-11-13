def is_prime(n):
    if n == 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for p in range(5, int(n ** 0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    return True


for case in range(1, int(input()) + 1):
    counter = {}
    for i in input():
        counter[i] = counter.get(i, 0) + 1

    result = []
    for i in sorted(counter):
        if is_prime(counter[i]):
            result.append(i)

    print(f'Case {case}: {"".join(result) if len(result) else "empty"}')
