_ = input()
data = list(map(int, input().split()))
for _ in range(int(input())):
    comm = list(map(int, input().split()))

    # push
    if comm[0] == 1:
        if 0 in data:
            data[data.index(0)] = comm[1]
    
    # erase
    elif comm[0] == 2:
        data[comm[1]] = 0
    
    # get
    else:
        if 0 in data:
            print(data.index(0))
        else:
            print(-1)