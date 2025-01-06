def interleave_array(arr):
    mid = len(arr) // 2
    rgt = iter(arr[mid:])
    iterator = (i for i in range(len(arr) - 2, 0, -2))
    for i in range(mid - 1, 0, -1):
        arr[next(iterator)] = arr[i]
    for i in range(1, len(arr), 2):
        arr[i] = next(rgt)

    return arr


print(interleave_array([1, 2, 3, 4, 5, 6, 7, 8]))
