def greater_prime(num):
    if num % 2 == 0:
        return num // 2
    if num % 3 == 0:
        return num // 3
    for i in range(5, num, 6):
        if num % i == 0:
            return num // i
        if num % (i + 2) == 0:
            return num // (i + 2)

print(greater_prime(int(input())))