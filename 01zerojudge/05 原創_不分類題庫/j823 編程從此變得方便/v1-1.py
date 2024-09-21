from sys import stdin


for line in stdin:
    line = line.strip()
    if line == 'stop': break
    line = line if line.isdigit() else f'"{line}"'
    print(f'print({line})')
