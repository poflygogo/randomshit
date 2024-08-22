from sys import stdin, stdout
from re import fullmatch

for line in stdin:
    match = [int(item) for item in line.split() if fullmatch(r'^\d+$', item)]

    if match:
        stdout.write(f'{sum(match)}\n')
    else:
        stdout.write('0\n')

# 來都來了，練習一下正則表達式