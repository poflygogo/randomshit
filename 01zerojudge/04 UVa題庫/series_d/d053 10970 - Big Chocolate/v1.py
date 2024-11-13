while True:
    try:
        data = tuple(map(int,input().split()))
    except EOFError:
        break
    else:
        print(data[0]*data[1]-1)
