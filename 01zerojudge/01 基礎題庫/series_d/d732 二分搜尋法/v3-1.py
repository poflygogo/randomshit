def binary_search(target: object, rgt: int, lft: int = 0) -> int:
    if rgt < lft:
        return 0
    
    mid = (rgt + lft) // 2
    if data[mid] == target:
        return mid + 1
    
    if data[mid] > target:
        return binary_search(target, rgt = mid - 1, lft = lft)
    
    return binary_search(target, rgt = rgt, lft = mid + 1)


length, _ = map(int, input().split())
data = [int(i) for i in input().split()]

for query in (int(i) for i in input().split()):
    print(binary_search(query, length -1))
