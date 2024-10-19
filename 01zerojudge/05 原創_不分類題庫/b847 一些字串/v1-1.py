from sys import stdin


for line in stdin:
    line = line.rstrip().upper()
    counter = [line.count(chr(i)) for i in range(65, 91)]
    total = sum(counter)
    ratios = [f'{i * 100 / total:.2f}' for i in counter]
    print(*counter)
    print(*ratios)
