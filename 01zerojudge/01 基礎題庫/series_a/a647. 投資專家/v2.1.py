for _ in range(int(input())):
    init, after = map(int, input().split())
    result = (after - init) / init * 100
    if result > 0:
        result += 0.00001
    elif result < 0:
        result -= 0.00001

    print(
        f'{result :2.2f}%',
        'dispose' if result >= 10 or result <= -7 else 'keep'
    )