base = int(input())

for i in input().split()[:-1]:
    i = int(i)
    if i % base == 0:
        print(i // base)
    else:
        print(base - i % base)    
