from sys import stdin, stdout

for num in stdin:
    num = int(num.strip())
    if not num:
        break

    result = 0
    while num > 0 and num % 2:
        result += 1
        num //= 2
    stdout.write(f'{result}\n')
    stdout.flush()