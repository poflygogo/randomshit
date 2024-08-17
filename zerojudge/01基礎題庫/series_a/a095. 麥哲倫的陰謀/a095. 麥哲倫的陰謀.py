while True:
    try:
        total, red = map(int ,input().split())
    except:
        break
    if total == red:
        print(red)
    else:
        print(red+1)
