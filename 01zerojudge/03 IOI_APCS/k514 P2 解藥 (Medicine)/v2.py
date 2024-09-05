ra, rb, rc, rd = map(int, input().split())
_ = input()
data_a = tuple(map(int, input().split()))
data_b = tuple(map(int, input().split()))
data_c = tuple(map(int, input().split()))
data_d = tuple(map(int, input().split()))

result = -1,
for a in data_a:
    for b in data_b:
        if ra * b != rb * a:
            continue
        for c in data_c:
            if ra * c != rc * a:
                continue
            for d in data_d:
                if ra * d == rd * a:
                    result = (a, b, c, d)
                    break
print(*result)