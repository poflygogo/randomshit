candy, kid = map(int, input().split())

if kid == 0:
    print('OK!')
else:
    candy %= kid
    if candy == 0:
        print('OK!')
    else:
        print(candy)