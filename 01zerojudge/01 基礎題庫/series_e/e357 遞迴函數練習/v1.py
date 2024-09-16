def myfunc(n:int) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return myfunc(n/2)
    else:
        return myfunc(n-1) + myfunc(n + 1)

print(myfunc(int(input())))