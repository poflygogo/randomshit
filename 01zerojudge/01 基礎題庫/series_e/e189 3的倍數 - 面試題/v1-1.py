from sys import stdin


def is_mul3(n: int) -> bool:
    while n > 0:
        n -= 3
    return n == 0


for num in stdin:
    num = sum([int(i) for i in num.strip()])
    print('YES' if is_mul3(num) else 'NO')
