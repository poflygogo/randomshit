num1, num2 = map(int, input().split())
if num1 % num2 == 0:
    print(f'整數 {num1 // num2}')
else:
    if num1 // num2 == 0:
        print(f'真分數 {num1}/{num2}')
    else:
        print(f'帶分數 {num1 // num2} {num1 % num2}/{num2}')