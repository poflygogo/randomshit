for _ in range(int(input())):
    add, sub = map(int, input().split())
    num1 = add + sub
    num2 = add - num1 / 2
    if num1 % 2 == 0 and num2 >= 0:
        print(f'{num1 // 2} {num2:.0f}')
    else:
        print('impossible')
