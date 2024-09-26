from sys import stdin


for num in stdin:
    num = int(num)
    print('no' if num % 3 else 'yes')
