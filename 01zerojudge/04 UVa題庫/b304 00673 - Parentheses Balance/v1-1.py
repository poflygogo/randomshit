match = {')': '(', ']': '['}
for _ in range(int(input())):
    stack = []
    for i in input().rstrip():
        if i in ('(', '['):
            stack.append(i)
            continue
        if stack and match[i] == stack.pop():
            continue
        else:
            print('No')
            break
    else:
        if stack:
            print('No')
        else:
            print('Yes')
