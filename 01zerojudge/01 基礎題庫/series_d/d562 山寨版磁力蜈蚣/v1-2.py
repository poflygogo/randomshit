from sys import stdin


for _ in stdin:
    data = stdin.readline().rstrip().split()
    print(*data)
    flag = True

    while len(data) > 0:
        if flag:
            del data[0]
            print(*data[::-1])
        else:
            del data[-1]
            print(*data)
        
        flag ^= True
