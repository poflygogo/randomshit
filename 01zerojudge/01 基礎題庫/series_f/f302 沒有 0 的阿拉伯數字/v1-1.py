def to_int(num_9base: str) -> int:
    res = 0
    for c in num_9base:
        res *= 9
        res += int(c)
    return res


print(to_int(input()))
