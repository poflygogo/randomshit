num1, operator, num2 = input().split()

if operator == '+': print(int(num1) + int(num2))
elif operator == '-': print(int(num1) - int(num2))
elif operator == '*': print(int(num1) * int(num2))
else: print(int(int(num1) / int(num2)))