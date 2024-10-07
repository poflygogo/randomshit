from sys import stdin
from itertools import chain


data = [[], [], [], [], []]
for _ in range(9):
    temp = stdin.readline().rstrip().split()
    del temp[0]
    for i in range(5):
        if temp:
            data[i].append(temp.pop(0))
        else:
            break

target = int(stdin.readline().rstrip())

state = [False] * 3
score, out = 0, 0
for item in chain(*data):
    if item[1] == 'B':
        state.extend([True] + [False] * (int(item[0]) - 1))
    elif item == 'HR':
        state.extend([True, False, False, False])
    else:
        out += 1
        target -= 1
        score += sum(state[:-3])

        if target == 0:
            print(score)
            break

        if out == 3:
            state = [False] * 3
            out = 0
        else:
            del state[:-3]
