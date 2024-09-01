for _ in range(int(input())):
    data = input().split()
    stack = []
    match data[0]:
        case '1':
            stack.append(data[1])
        case '2':
            print(stack[-1] if stack else -1)
        case '3':
            del stack[-1]