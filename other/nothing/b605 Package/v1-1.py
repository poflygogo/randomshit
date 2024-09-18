from sys import stdin


for line in stdin:
    line = [int(i) for i in line.strip().split()]
    if line [0] == -1:
        break

    