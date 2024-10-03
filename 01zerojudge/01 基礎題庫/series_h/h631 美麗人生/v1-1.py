n = int(input())

for p in (2, 3, 5):
    while n % p == 0:
        n //= p

print(
    'ugly' if n == 1 else 'beautiful'
)
