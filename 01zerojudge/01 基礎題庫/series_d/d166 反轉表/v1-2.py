from sys import stdin


for line in stdin:
    line = [int(i) for i in line.strip().split()]
    if line == -1: break

    result = [0] * len(line)
    for i in range(len(line)):
        count = 0
        for j in range(len(line)):
            if result[j] == 0 or result[j] > i + 1:
                count += 1
            if count == line[i] + 1:
                result[j] = i + 1
                break

    print(*result)
