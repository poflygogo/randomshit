from sys import stdin


for line in stdin:
    line = line.rstrip()
    if len(line) < 3:
        print('1/1')
    
    idx, cnt = 0, 0
    while idx < len(line):
        if line[idx] == 'R' and idx + 3 <= len(line) and line[idx:idx + 3] == 'RED':
            cnt += 1
            idx += 3
        elif line[idx] == 'G' and idx + 5 <= len(line) and line[idx:idx + 5] == 'GREEN':
            cnt += 1
            idx += 5
        else:
            idx += 1
    print(f'1/{2 ** cnt}')
