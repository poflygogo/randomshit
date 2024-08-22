stack = []
for _ in range(int(input())):
    data = tuple(map(int, input().split()))
    if data[0] == 1:
        stack.append(data[1])
    elif data[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        if len(stack) != 0:
            del stack[-1]