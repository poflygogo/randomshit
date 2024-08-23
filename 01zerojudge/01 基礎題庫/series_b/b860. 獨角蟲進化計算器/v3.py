candy, weedle = map(int, input().split())

candy += weedle

if candy < 13:
    print(0)
else:
    t = int((candy - 13)/11) + 1
    if t >= weedle:
        print(weedle)
    else:
        print(t)