from sys import stdin


for num in stdin:
    num = num.rstrip()
    if num == '-1':
        exit()
    elif '0x' in num:
        print(int(num[2:], 16))
    else:
        print(hex(int(num)).upper().replace('X', 'x', 1))
