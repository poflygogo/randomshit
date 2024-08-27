def operate(operator:str, num1:int, num2:int):
    if operator == '+':
        return num2 + num1
    if operator == '-':
        return num2 - num1
    if operator == '*':
        return num2 * num1
    if operator == '/':
        return num2 / num1
    
data = input().split()

stack = []
for item in data:
    if item in '+-*/':
        stack.append(
            operate(item, stack.pop(-1), stack.pop(-1))
        )
    else:
        stack.append(int(item))

print(stack[0])