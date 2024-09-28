from sys import stdin


for _ in stdin:
    data = stdin.readline().rstrip().split()
    lft, rgt = 0, len(data) - 1
    flag = True
    while lft <= rgt:
        if flag:
            print(*data[lft: rgt + 1])
            lft += 1
        else:
            print(*data[rgt: lft - 1: -1])
            rgt -= 1
        
        flag ^= True
