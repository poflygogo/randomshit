input()
data = input().split()
for i in sorted(set(data)):
    print(i, data.count(i))
