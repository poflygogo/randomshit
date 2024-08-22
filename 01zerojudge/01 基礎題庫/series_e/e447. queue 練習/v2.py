from sys import stdin, stdout
from collections import deque

queue = deque()
_ = stdin.readline()
for command in stdin:
    command = command.strip().split()
    if command[0] == '1':
        queue.append(command[1])

    elif command[0] == '2':
        if queue:
            stdout.write(f'{queue[0]}\n')
        else:
            stdout.write('-1\n')

    elif queue:
        del queue[0]