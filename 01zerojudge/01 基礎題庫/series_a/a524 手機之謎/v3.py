from sys import stdout
from itertools import permutations

while True:
    try:
        line = int(input())
    except EOFError:
        break

    data = [str(i) for i in range(1, line + 1)]
    data = sorted(permutations(data), reverse=True)

    for i in data:
        result =''.join(i)
        stdout.write(result + '\n')