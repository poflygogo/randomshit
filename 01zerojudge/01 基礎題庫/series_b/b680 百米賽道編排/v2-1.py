from sys import stdin


# input data
total = int(stdin.readline().rstrip())
players = [(lambda x, y: (int(x), float(y)))(*stdin.readline().rstrip().split()) for _ in range(total)]
players.sort(key=lambda x: x[1])

# group
groups_cnt = total // 8
for i in range(groups_cnt):
    out = []
    for j in range(i, total, groups_cnt * 2):
        out.extend([players[j], players[j + groups_cnt * 2 - i * 2 - 1]])

    print(i + 1, *[out[k - 1][0] for k in (7, 5, 3, 1, 2, 4, 6, 8)])
