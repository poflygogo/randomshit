from sys import stdin


for num in stdin:
    num = num.strip()
    if num[-1] in '02468':
        print(num)
    else:
        print(int(num) - 1)
