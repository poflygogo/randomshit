from sys import stdin, stdout

for n in stdin:
    if int(n) % 9 != 0 or int(n) == 0:
        stdout.write(f'{int(n) % 9}\n')
        continue

    stdout.write('9\n')