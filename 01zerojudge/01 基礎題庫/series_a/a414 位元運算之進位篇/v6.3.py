while True:
    num = int(input())
    if not num:
        break

    result = 0
    while num > 0 and num % 2:
        result += 1
        num //= 2
    print(result)