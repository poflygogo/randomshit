while True:
    length = int(input())
    if length == 0: break
    numlist = sorted(list(map(int, input().split())), reverse=True)

    cost = 0
    for index, num in enumerate(numlist):
        cost += num * (index + 1)
    cost -= numlist[-1]

    print(cost)