import sys

for num in sys.stdin:
    num = int(num.strip())
    factors = []
    prime = 2
    while num >= prime:
        if num % prime:
            prime += 1
        else:
            factors.append(prime)
            num //= prime
    
    print(sum(factors))