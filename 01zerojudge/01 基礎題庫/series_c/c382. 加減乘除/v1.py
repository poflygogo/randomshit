num1, operator, num2 = list(map(lambda n: int(n) if n.isdecimal() else n, input().split()))

if operator == '+': print(num1 + num2)
elif operator == '-': print(num1 - num2)
elif operator == '*': print(num1 * num2)
else: print(int(num1 / num2))