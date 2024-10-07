from sys import stdin


data = [stdin.readline().rstrip().split()[1:] for _ in range(9)]
target = int(stdin.readline().rstrip())

state = 0
score, out = 0, 0
for i, j in ((_i, _j) for _i in range(5) for _j in range(9)):
    if data[j][i][1] == 'B':
        state <<= 1
        state += 1
        state <<= int(data[j][i][0]) - 1

    elif data[j][i] == 'HR':
        state <<= 1
        state += 1
        state <<= 3

    else:
        out += 1
        target -= 1
        score += sum(int(i) for i in bin(state & -8)[2:])

        if target == 0:
            print(score)
            break

        if out == 3:
            state = 0
            out = 0
        else:
            state &= 7
