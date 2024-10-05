n = int(input())
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    prev1, prev2 = 0, 1
    n -= 2
    while n > 0:
        prev1, prev2 = prev2, prev1 + prev2
        n -= 1
    print(prev2)
