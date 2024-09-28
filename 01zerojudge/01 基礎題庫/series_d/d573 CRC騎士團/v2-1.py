from sys import stdin


for l in stdin:
    group = []
    numbers = []
    for _ in range(int(l)):
        s = stdin.readline().rstrip().split()
        group.append(s.pop(0))
        del s[0]
        numbers.append(s)
    
    target = stdin.readline().rstrip()
    for i in range(int(l)):
        if target in numbers[i]:
            print(group[i])
            break
