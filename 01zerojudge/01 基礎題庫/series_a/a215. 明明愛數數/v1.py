def minminlovecount(n,m):
    total = 0
    count = 0
    while True:
        total += n
        count += 1
        n += 1
        if total > m:break
    print(count)

while True:
    try:n, m = map(int,input().split())
    except EOFError:break
    minminlovecount(n,m)
