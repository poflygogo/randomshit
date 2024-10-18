base = int(input())
data = input().split()
del data[-1]

for i in data:
    i = int(i)
    if i % base == 0:
        print(i // base)
    else:
        print(base - i % base)    
