from sys import stdin


for i in stdin:
    data = {}
    for _ in range(int(i)):
        s = stdin.readline().rstrip().split()
        group = s.pop(0)
        del s[0]
        data.update({group:s})
    
    target = stdin.readline().rstrip()
    for i in data:
        if target in data[i]:
            print(i)
            break
