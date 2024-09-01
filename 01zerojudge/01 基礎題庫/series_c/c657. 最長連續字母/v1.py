import itertools

while True:
    try:
        data = [(i, len(tuple(j))) for i, j in itertools.groupby(input())]
    except EOFError:
        break
    
    result = max(data, key= lambda x: x[1])
    print(*result)