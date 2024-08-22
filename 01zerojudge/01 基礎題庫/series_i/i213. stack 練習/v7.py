from sys import stdin, stdout

stdin.readline()
stack = []
for line in stdin:
    if line[0] == '1':
        stack.append(line[2])
    elif line[0] == '2':
        if stack:
            stdout.write(f'{stack[-1]}\n')
        else:
            stdout.write('-1\n')
    elif stack:
        del stack[-1]