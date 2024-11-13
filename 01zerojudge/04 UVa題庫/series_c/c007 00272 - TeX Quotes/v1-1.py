from sys import stdin


for line in stdin:
    line = line.rstrip()
    counter = line.count('"')
    while counter % 2 != 0:
        line += '\n' + next(stdin).rstrip()
        counter = line.count('"')
    for _ in range(counter // 2):
        line = line.replace('"', '``', 1).replace('"', '\'\'', 1)
    print(line)
