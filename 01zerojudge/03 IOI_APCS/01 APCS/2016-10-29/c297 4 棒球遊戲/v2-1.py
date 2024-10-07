from sys import stdin
from collections import deque


data = [stdin.readline().rstrip().split()[1:] for _ in range(9)]
target = int(stdin.readline().rstrip())

state = deque([False, False, False])
score, out = 0, 0
for i, j in ((_i, _j) for _i in range(5) for _j in range(9)):
    if data[j][i][1] == 'B':
        score += state.popleft()
        state.append(True)
        for _ in range(int(data[j][i][0]) - 1):
            score += state.popleft()
            state.append(False)
    
    elif data[j][i] == 'HR':
        score += sum(state) + 1
        state = deque([False, False, False])
    
    else:
        out += 1
        target -= 1

        if target == 0:
            print(score)
            break

        if out == 3:
            state = deque([False, False, False])
            out = 0
