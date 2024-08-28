from sys import stdin, stdout

for num in stdin:
    num = int(num)
    if not num:
        break

    num1_bit, num2_bit = format(num, 'b'), format(num + 1, 'b')
    result = sum([1 for i, j in zip(num1_bit[::-1], num2_bit[::-1]) if i != j and i == '1'])
    stdout.write(f'{result}\n')