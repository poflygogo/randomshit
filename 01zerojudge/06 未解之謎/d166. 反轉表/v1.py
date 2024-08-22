from sys import stdin

for line in stdin:
    line = line.strip()
    if line in ('', '-1'): continue

    line = tuple(map(int, line.split()))
    result = [0 for _ in range(len(line))]

    for idx, item in enumerate(line):
        count = 0
        for jdx, j in enumerate(result):
            if count >= item:
                if result[jdx] == 0:
                    result[jdx] == idx + 1
                    break
            elif j == 0:
                count += 1
    
    print(result)