from sys import stdin, stdout

for num in stdin:
    num = bin(int(num))
    if num == '0b0':
        break

    stdout.write(f'{len(num) - len(num.rstrip("1"))}\n')