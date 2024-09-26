from sys import stdin


output = []
stack1, stack2 = 0, 0
for command in stdin:
    command = command.strip().split()
    # 如果 command 是 push
    if command[0] == 'push':
        output.append(1)
        stack1 += 1

    # 如果是 pop，檢查 stack2 內的元素數量
    elif stack2 > 0:
        output.append(4)
        stack2 -= 1

    else:
        output.extend([5 for _ in range(stack1)] + [4])
        stack2 = stack1 - 1
        stack1 = 0

print(*output, sep='')
