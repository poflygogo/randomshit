from sys import stdin

stdin.readline()
stack = []
for line in stdin:
    data = tuple(map(int, line.split()))
    if data[0] == 1:
        stack.append(data[1])
    elif data[0] == 2:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        if stack:
            del stack[-1]