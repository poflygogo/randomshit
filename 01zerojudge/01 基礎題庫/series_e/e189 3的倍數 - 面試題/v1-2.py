from sys import stdin


def is_mul3(n: int) -> bool:
    if n > 30:
        return is_mul3(n - 30)
    if n > 15:
        return is_mul3(n - 12)
    if n > 0:
        return is_mul3(n - 3)
    return n == 0


for num in stdin:
    num = sum([int(i) for i in num.strip()])
    print('YES' if is_mul3(num) else 'NO')
