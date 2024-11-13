from sys import stdin


flag = True
for line in stdin:
    line = line.rstrip()
    for _ in range(line.count('"')):
        line = line.replace('"', '``' if flag else '\'\'', 1)
        flag = not flag
    print(line)
