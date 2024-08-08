def minminlovecount(n,m):
    total = 0
    n_end = n
    while True:
        total += n_end
        n_end += 1
        if total > m: break
    print(n_end-n)

while True:
    try:n, m = map(int,input().split())
    except EOFError:break
    minminlovecount(n,m)
