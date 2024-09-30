from sys import stdin


for line in stdin:
    line = line.rstrip().replace('or', '||').replace('and', '&&').split()

    expr = ''.join(line)
    result = int(line.pop(0), 2)
    while line:
        op = line.pop(0)
        if op == '&&':
            result &= int(line.pop(0), 2)
        else:
            result |= int(line.pop(0), 2)
    
    print(f'{expr} = {bin(result)[2:].zfill(5)}')
