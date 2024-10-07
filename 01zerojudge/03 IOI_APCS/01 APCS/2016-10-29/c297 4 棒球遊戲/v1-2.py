from sys import stdin


data = [stdin.readline().rstrip().split()[1:] for _ in range(9)]
target = int(stdin.readline().rstrip())

state = [False] * 3
score, out = 0, 0
for i, j in ((_i, _j) for _i in range(5) for _j in range(9)):
    if data[j][i][1] == 'B':
        state.extend([True] + [False] * (int(data[j][i][0]) - 1))
    elif data[j][i] == 'HR':
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
            state = state[-3:]
