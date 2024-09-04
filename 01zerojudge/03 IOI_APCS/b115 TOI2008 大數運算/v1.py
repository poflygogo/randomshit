import sys

for num1 in sys.stdin:
    num1 = num1.strip()
    a = next(sys.stdin).strip()
    num2 = next(sys.stdin).strip()
    if a == '*':
        print(int(num1) * int(num2))
    else:
        print(int(num1) // int(num2))