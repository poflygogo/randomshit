from sys import stdin


for line in stdin:
    line = line.rstrip().split()
    if not line:
        break
    print(
        f'{" ".join(line)}.',
        'I will make it!' if int(line[1]) / int(line[2]) <= int(line[0])
        else 'I will be late!'
    )
