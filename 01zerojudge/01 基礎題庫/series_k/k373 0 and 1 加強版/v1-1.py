from sys import stdin


data = []
for line in stdin:
    line = line.rstrip().split()
    if line[1] == '0' and line[0] not in data:
        data.append(line[0])
print(*data, sep='\n')
