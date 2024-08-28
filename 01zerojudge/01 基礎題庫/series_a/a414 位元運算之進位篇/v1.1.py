from sys import stdin, stdout

for num in stdin:
    num = int(num)
    if not num:
        break

    num_bit = format(num, 'b')
    stdout.write(f'{len(num_bit)-len(num_bit.rstrip("1"))}\n')