def binary_search(target: object) -> int:
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


length = int(input().split()[0])
data = input().split()

for query in input().split():
    print(binary_search(query))
