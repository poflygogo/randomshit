num = int(input())

if num <= 3:
    print('yes')
elif num % 2 == 0:
    print('no')
elif num % 3 == 0:
    print('no')
else:
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0:
            print('no')
            break
        elif num % (i + 1):
            print('no')
            break
    else:
        print('yes')