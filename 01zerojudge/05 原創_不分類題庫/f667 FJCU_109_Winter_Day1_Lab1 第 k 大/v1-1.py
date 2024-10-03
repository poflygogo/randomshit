from sys import stdin


data = []
for i in stdin:
    i = int(i.rstrip())
    if i == -1:
        break
    data.append(i)
data.sort()
print(data[-int(stdin.readline().rstrip())])
