from sys import stdin


# input data
total = int(stdin.readline().rstrip())
players = [(lambda x, y: (int(x), float(y)))(*stdin.readline().rstrip().split()) for _ in range(total)]
players.sort(key=lambda x: x[1])

# group
groups_cnt = total // 8
flag, idx = True, 0
groups = [[] for i in range(groups_cnt)]
for item in players:
    groups[idx].append(item[0])
    if flag:
        idx += 1
    else:
        idx -= 1
    
    if idx == groups_cnt:
        flag ^= True
        idx -= 1
    elif idx < 0:
        flag ^= True
        idx += 1

# output
for i, data in enumerate(groups):
    print(i + 1, *[data[k - 1] for k in (7, 5, 3, 1, 2, 4, 6, 8)])
