import sys

for num in sys.stdin:
    num = int(num.strip())
    if not num:
        break

    result = 0
    while num > 0 and num % 2:
        result += 1
        num //= 2
    sys.stdout.write(f'{result}\n')