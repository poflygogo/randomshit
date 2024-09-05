def is_prime(num):
    if num == 1: return False
    if num % 2 == 0: return False
    if num % 3 == 0: return False

    for i in range(5, int(num ** (1/2)) + 1, 6):
        if num % i == 0: return False
        if num % (i + 2) == 0: return False
    return True

for _ in range(int(input())):
    print('Y' if is_prime(int(input())) else 'N')