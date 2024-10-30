def func(n: int):
    if n < 10:
        return n
    return func(sum(map(int, str(n))))


while True:
    num = int(input())
    if not num:
        exit()
    print(func(num))
