for _ in range(int(input())):
    n = int(input())
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print('a leap year')
    else:
        print('a normal year')