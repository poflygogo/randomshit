a1, an, diff = map(int, input().split())

if diff > 0:
    for i in range(a1, an+1, diff):
        print(i,end=" ")
elif diff < 0:
    for i in range(a1, an-1, diff):
        print(i,end=" ")
else:
    print(a1)
