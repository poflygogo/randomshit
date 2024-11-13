def is_happy_number(n: int) -> bool:
    data = []
    while n not in data and n != 1:
        data.append(n)
        check = []
        while n > 0:
            check.append((n % 10) ** 2)
            n //= 10
        n = sum(check)
    return n == 1


for i in range(1, int(input()) + 1):
    num = int(input())
    print(f'Case #{i}: {num} is {"a H" if is_happy_number(num) else "an Unh"}appy number.')
