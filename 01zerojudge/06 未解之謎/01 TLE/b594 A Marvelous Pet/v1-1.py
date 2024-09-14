from sys import stdin


for n in stdin:
    n = int(n)
    if not n: break

    max_k = n // 2 + 1
    check = 0
    count = 0
    while max_k > 0:
        for k in range(max_k, 0, -1):
            check += k
            if check < n: continue
            if check == n: count += 1
            break
        max_k -= 1
        check = 0
    print(count)
