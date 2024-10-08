def get_min_group(cost:list, maxcost:int) -> int:
    cost.sort()
    left, right = 0, len(cost) - 1
    group = 0
    while left <= right:
        if maxcost >= cost[left] + cost[right]:
            left += 1
            right -= 1
        else:
            right -= 1
        group += 1
    return group

maxcost = int(input())
data = [int(input()) for _ in range(int(input()))]
print(get_min_group(data, maxcost))