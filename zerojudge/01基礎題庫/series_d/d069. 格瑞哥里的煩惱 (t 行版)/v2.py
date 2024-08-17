from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print('a leap year')
    else:
        print('a normal year')