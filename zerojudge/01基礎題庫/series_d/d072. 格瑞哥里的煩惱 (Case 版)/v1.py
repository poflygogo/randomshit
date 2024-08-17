for i in range(int(input())):
    n = int(input())
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print(f'Case {i+1}: a leap year')
    else:
        print(f'Case {i+1}: a normal year')