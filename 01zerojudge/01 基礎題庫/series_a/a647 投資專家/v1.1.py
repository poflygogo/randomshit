for _ in range(int(input())):
    init, after = map(int, input().split())
    result = round((after - init) / init * 100, 2)

    print(
        f'{result :2.2f}%',
        'dispose' if result >= 10 or result <= -7 else 'keep'
    )