num = int(input())

flag = True
if num in (2, 3, 5, 7):
    pass
elif num % 2 == 0 or num % 3 == 0:
    flag = False
else:
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0:
            flag = False
            break
        elif num % (i + 2) == 0:
            flag = False
            break

if flag:
    print('yes')
else:
    print('no')