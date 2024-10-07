from sys import stdin


data = [stdin.readline().rstrip().split()[1:] for _ in range(9)]
target = int(stdin.readline().rstrip())

a, b, c = 0, 0, 0
score, out = 0, 0
for i, j in ((_i, _j) for _i in range(5) for _j in range(9)):
    if data[j][i][1] == 'B':
        if data[j][i][0] == '1':
            score += a
            a, b, c = b, c, 1
        elif data[j][i][0] == '2':
            score += a + b
            a, b, c = c, 1, 0
        else:
            score += sum((a, b, c))
            a, b, c = 1, 0, 0
    
    elif data[j][i] == 'HR':
        score += sum((a, b, c)) + 1
        a, b, c = 0, 0, 0
    
    else:
        out += 1
        target -= 1

        if target == 0:
            print(score)
            break

        if out == 3:
            a, b, c = 0, 0, 0
            out = 0
