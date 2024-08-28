from sys import stdin, stdout

for num in stdin:
    num = int(num.strip()) + 1
    if num == 1:
        break

    stack = []
    while num > 1:
        item = num % 2
        if item == 1:
            break
        stack.append(item)
        num //= 2
    stdout.write(f'{len(stack)}\n')