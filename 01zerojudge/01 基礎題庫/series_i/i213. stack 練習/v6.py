from sys import stdin, stdout

stdin.readline()
stack = []
for line in stdin:
    data = tuple(map(int, line.split()))
    if data[0] == 1:
        stack.append(data[1])
    elif data[0] == 2:
        if stack:
            stdout.write(f'{stack[-1]}\n')
        else:
            stdout.write('-1\n')
    elif stack:
        del stack[-1]