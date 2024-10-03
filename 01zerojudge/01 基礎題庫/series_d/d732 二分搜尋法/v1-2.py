def binary_search(target: int) -> int:
    lft, rgt = 0, length - 1

    while lft <= rgt:
        mid = (rgt + lft) // 2
        if data[mid] == target:
            return mid + 1
        if data[mid] > target:
            rgt = mid - 1
        else:
            lft = mid + 1
    return 0


length, _ = map(int, input().split())
data = [int(i) for i in input().split()]

for query in (int(i) for i in input().split()):
    print(binary_search(query))
