ra, rb, rc, rd = map(int, input().split())
r_sum = sum((ra, rb, rc, rd))
rsa, rsb, rsc, rsd = ra/r_sum, rb/r_sum, rc/r_sum, rd/r_sum
_ = input()
data_a = tuple(map(int, input().split()))
data_b = tuple(map(int, input().split()))
data_c = tuple(map(int, input().split()))
data_d = tuple(map(int, input().split()))

result = -1,
for a in data_a:
    for b in data_b:
        for c in data_c:
            for d in data_d:
                sum = a + b + c + d
                if a / sum == rsa and \
                    b / sum == rsb and \
                    c / sum == rsc and \
                    d / sum == rsd:
                    result = (a, b, c, d)
                    break
print(*result)