from sys import stdin, stdout

for num in stdin:
    num = int(num)
    if not num:
        break
    
    num = bin(num)
    result = 0
    for i in num[-1:1:-1]:
        if i == '1':
            result += 1
        else:
            break
    stdout.write(f'{result}\n')