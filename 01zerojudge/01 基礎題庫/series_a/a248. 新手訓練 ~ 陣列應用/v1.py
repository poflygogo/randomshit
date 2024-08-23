from sys import stdin

for line in stdin:
    try:
        a, b, N = map(int, line.strip().split())
    except ValueError:
        continue
    
    result = str(a // b) + '.'
    remain = a % b
    if remain == 0:
        result += '0' * N
    else:
        result += str(remain * (10 ** N) // b)

    print(result)