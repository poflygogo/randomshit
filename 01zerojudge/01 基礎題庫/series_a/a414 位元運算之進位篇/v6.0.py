from sys import stdin, stdout

for num in stdin:
    num = int(num.strip()) + 1
    if num == 1:
        break

    stack = []
    while num // 2:
        stack.append(num % 2)
        num //= 2
    stack.append(num % 2)
    stdout.write(f'{stack.index(1)}\n')