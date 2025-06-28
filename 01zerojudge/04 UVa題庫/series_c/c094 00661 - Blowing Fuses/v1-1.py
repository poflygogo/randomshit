# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00661 Blowing Fuses
# ZeroJudge c094


TEXT_FAIL = "Fuse was blown."
TEXT_SUCCEED = "Fuse was not blown.\nMaximal power consumption was {} amperes."
test_case = 1
n, m, c = map(int, input().split())
while not n == m == c == 0:
    data = {i: int(input()) for i in range(1, n + 1)}
    used = set()
    amperes_curr = amperes_max = 0
    for _ in range(m):
        t = int(input())
        if amperes_max > c:
            continue
        if t in used:
            amperes_curr -= data[t]
            used.remove(t)
        else:
            amperes_curr += data[t]
            used.add(t)
            amperes_max = max(amperes_max, amperes_curr)

    if test_case > 1:
        print()
    print(
        f"Sequence {test_case}",
        TEXT_FAIL if amperes_max > c else TEXT_SUCCEED.format(amperes_max),
        sep="\n"
    )

    test_case += 1
    n, m, c = map(int, input().split())
