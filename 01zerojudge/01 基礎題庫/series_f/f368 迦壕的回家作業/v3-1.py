from sys import stdin


for line in stdin:
    line = line.rstrip()
    print(f'1/{2 ** (line.count("RED") + line.count("GREEN"))}')
