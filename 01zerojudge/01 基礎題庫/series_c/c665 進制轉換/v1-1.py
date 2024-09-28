from sys import stdin


numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for line in stdin:
    n, b1, b2 = line.rstrip().split()
    n = int(n, base=int(b1))
    b2 = int(b2)

    result = []
    while n > 0:
        result.append(numbers[n % b2])
        n //= b2
    
    print(*reversed(result), sep='')
