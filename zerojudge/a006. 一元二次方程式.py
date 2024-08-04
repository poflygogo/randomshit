a, b, c = map(int, input().split())
checkN = b ** 2 - 4 * a * c
if checkN < 0:
    print('No real root')
else:
    n = checkN ** (1 / 2)
    ansA = int((-b + n) / (2 * a))
    ansB = int((-b - n) / (2 * a))
    if ansA > ansB:
        print(f'Two different roots x1={ansA} , x2={ansB}')
    elif ansA < ansB:
        print(f'Two different roots x1={ansB} , x2={ansA}')
    else:
        print(f'Two same roots x={ansA}')
