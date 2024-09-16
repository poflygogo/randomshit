def permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        curr = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([curr] + p)
    return result

def combinations(arr, r):
    if r == 0:
        return [[]]
    if len(arr) < r:
        return []
    result = []
    for i in range(len(arr) - r + 1):
        head = arr[i:i+1]
        tail = combinations(arr[i+1:], r-1)
        for c in tail:
            result.append(head + c)
    return result