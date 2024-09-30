from sys import stdin


for line in stdin:
    line = line.rstrip().replace('or', '||').replace('and', '&&').split()

    expr = ''.join(line)
    line = iter(line)
    result = int(next(line), 2)
    for op in line:
        if op == '&&':
            result &= int(next(line), 2)
        else:
            result |= int(next(line), 2)
    
    print(f'{expr} = {bin(result)[2:].zfill(5)}')
