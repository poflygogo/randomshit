from sys import stdin


def get_ans(n: int):
    if n < 5: return 0
    n //= 5
    return n + get_ans(n)


for num in stdin:
    num = int(num)
    print(get_ans(num))
