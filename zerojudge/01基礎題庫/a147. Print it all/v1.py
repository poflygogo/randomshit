while True:
    n = int(input())
    if n == 0:break
    numbers = []
    for i in range(1,n):
        if i % 7 != 0:
            numbers.append(i)
    print(*numbers)
