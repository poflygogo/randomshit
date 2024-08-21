num = int(input())

if num in (2, 3, 5, 7):
    print('yes')
elif num % 2 == 0:
    print('no')
elif num % 3 == 0:
    print('no')
else:
    for i in range(5, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            print('no')
            break
    else:
        print('yes')