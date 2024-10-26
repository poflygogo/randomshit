from sys import stdin


lower, larger = [], []
for n in stdin:
    larger.append(int(n.rstrip()))
    if lower and larger and max(lower) > min(larger):
        lower.append(larger.pop(larger.index(min(larger))))

    if len(lower) > len(larger) + 1:
        larger.append(lower.pop(lower.index(max(lower))))
    elif len(larger) > len(lower):
        lower.append(larger.pop(larger.index(min(larger))))

    if len(lower) > len(larger):
        print(max(lower))
    else:
        print((max(lower) + min(larger)) // 2)
