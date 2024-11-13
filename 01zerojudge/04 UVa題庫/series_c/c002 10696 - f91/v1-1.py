def f91(n: int) -> int:
    if n <= 100:
        return f91(f91(n + 11))

    else:
        return n - 10


while True:
    num = int(input())
    if not num:
        exit()
    
    print(f'f91({num}) = {f91(num)}')
