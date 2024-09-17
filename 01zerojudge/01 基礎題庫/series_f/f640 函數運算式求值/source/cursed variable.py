def 加(a, b):
    return a + b

def 減(a, b):
    return a - b

前序運算式 = ['+', 2, '-', 3, 1]
stack = []

# 從後面開始讀取
for item in reversed(前序運算式):
    if item not in ('+', '-'):
        stack.append(item)
    else:
        # 檢查運算子是什麼，決定要用什麼函數
        if item == '+':
            stack.append(加(stack.pop(), stack.pop()))
        elif item == '-':
            stack.append(減(stack.pop(), stack.pop()))

print(stack.pop())


