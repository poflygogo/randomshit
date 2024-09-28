from itertools import groupby


while True:
    try:
        length1 = input()
    except EOFError:
        break

    if length1.isdigit():
        length1 = int(length1)
        data = input()
    else:
        length1, data = length1.split()
        length1 = int(length1)
    
    result = []
    for key, val in groupby(data):
        length2 = len(tuple(val))
        result.extend([str(length2), str(key)])
    
    if length1 <= len(result):
        print(data)
    else:
        print(*result, sep='')
