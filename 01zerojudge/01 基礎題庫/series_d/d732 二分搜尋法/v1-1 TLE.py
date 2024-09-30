def binary_search(target: object) -> int:
    lft, rgt = 0, length
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if data[mid] == target:
            return mid + 1
        
        if data[mid] > target:
            rgt = mid
        
        else:
            lft = mid
    return 0


length, _ = map(int, input().split())
data = [int(i) for i in input().split()]

for query in [[int(i) for i in input().split()]]:
    print(binary_search(query))
