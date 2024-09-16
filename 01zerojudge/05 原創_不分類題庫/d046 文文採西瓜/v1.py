ability = int(input())
watermelen = tuple(map(int, input().split()))

print(sum([1 for i in watermelen if i <= 10]))