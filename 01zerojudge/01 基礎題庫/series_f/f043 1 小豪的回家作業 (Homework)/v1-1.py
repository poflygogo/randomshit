result, num1 = map(int, input().split())
if result == num1:
    num1 -= 3

num2 = result - num1
if num1 < num2:
    print(f'{num1}+{num2}={result}')
else:
    print(f'{num2}+{num1}={result}')
