num = int(input())

prime = set()
check = 2
while num >= check:
    if num % check:
        check += 1
    else:
        prime.add(check)
        num //= check

print(*sorted(list(prime)))