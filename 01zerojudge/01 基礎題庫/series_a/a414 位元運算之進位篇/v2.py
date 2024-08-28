from sys import stdin, stdout

for num in stdin:
    num = int(num)
    if not num:
        break

    num1_bit, num2_bit = format(num, 'b'), format(num + 1, 'b')
    if len(num2_bit) > len(num1_bit):
        stdout.write(f'{len(num1_bit)}\n')
    
    else:
        result = 0
        for i in zip(num1_bit[::-1], num2_bit[::-1]):
            if i == ('1', '0'):
                result += 1
            else:
                break
        stdout.write(f'{result}\n')