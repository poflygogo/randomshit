from math import sqrt


def grouper(iterable, n):
    # grouper('ABCDEFGHI', 3) → ABC DEF GHI
    iterators = [iter(iterable)] * n
    return zip(*zip(*iterators))


for _ in range(int(input())):
    code = input()
    length_sqrt = sqrt(len(code))
    if not length_sqrt.is_integer():
        print('INVALID')
    
    else:
        result = []
        for i in grouper(code, int(length_sqrt)):
            result.append(''.join(i))
        
        print(*result, sep='')
