def is_happy_number(n: int) -> bool:
    data = []
    while n not in data and n != 1:
        data.append(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


for i in range(1, int(input()) + 1):
    num = int(input())
    print(f'Case #{i}: {num} is {"a H" if is_happy_number(num) else "an Unh"}appy number.')
