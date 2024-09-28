from sys import stdin


for i in stdin:
    data = {}
    for _ in range(int(i)):
        s = stdin.readline().rstrip().split()
        group = s.pop(0)
        del s[0]
        data.update({i:group for i in s})
    print(data[stdin.readline().rstrip()])
