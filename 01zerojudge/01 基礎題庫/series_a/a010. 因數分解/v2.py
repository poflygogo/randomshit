num = int(input())
primes = []
check = 2

while num >= check:
    if num % check == 0:
        num //= check
        primes.append(check)
    else:
        check += 1

ans = []
for n in sorted(list(set(primes))):
    count = primes.count(n)
    if count > 1:
        ans.append(f'{n}^{count}')
    else:
        ans.append(n)

print(*ans, sep=' * ')