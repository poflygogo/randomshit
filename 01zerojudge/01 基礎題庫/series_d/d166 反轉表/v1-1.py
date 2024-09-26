from sys import stdin


for line in stdin:
    line = [int(i) for i in line.strip().split()]
    if line == -1: break

    result = [0] * len(line)
    for num, item in enumerate(line):
        count = 0
        for i, j in enumerate(result):
            if j == 0 and count == item:
                result[i] = num + 1
                break
            if j == 0 or j > num:
                count += 1

    print(*result)
