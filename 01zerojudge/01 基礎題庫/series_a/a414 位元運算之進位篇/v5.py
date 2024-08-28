from sys import stdin, stdout

for num in stdin:
    if num.strip() == '0':
        break
    num = bin(int(num) + 1)

    stdout.write(f'{num[-1:1:-1].index("1")}\n')