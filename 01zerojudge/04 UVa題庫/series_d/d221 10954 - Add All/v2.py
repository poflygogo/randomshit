while True:
    length = int(input())
    if length == 0: break
    numlist = list(sorted(map(int, input().split())))
    
    costlist = []
    for _ in range(length-1):
        cost = numlist.pop(0)
        cost += numlist.pop(0)
        numlist.append(cost)
        costlist.append(cost)
        numlist.sort()
    
    print(sum(costlist))