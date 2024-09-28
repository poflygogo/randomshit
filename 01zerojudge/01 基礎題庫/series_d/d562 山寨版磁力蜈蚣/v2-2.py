from sys import stdin


for _ in stdin:
    data = stdin.readline().rstrip().split()
    lft, rgt = 0, len(data) - 1
    flag = True
    while lft <= rgt:
        if flag:
            for i in range(lft, rgt):
                print(data[i], end=' ')
            print(data[rgt])
            lft += 1
        else:
            for i in range(rgt, lft, -1):
                print(data[i], end=' ')
            print(data[lft])
            rgt -= 1
        
        flag ^= True
