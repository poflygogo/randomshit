# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q879. I love physics


# 公式 -> (v裝 + v人) * 海水密度 = (m裝 + m人)

# 每個元素依序為 v人, m人, v裝, m裝, 海水密度
calc = [
    lambda _, b, c, d, e: (b + d) / e - c,
    lambda a, _, c, d, e: (a + c) * e - d,
    lambda a, b, _, d, e: (b + d) / e - a,
    lambda a, b, c, _, e: (a + c) / e - b,
    lambda a, b, c, d, _: (b + d) / (a + c),
]

while True:
    try:
        expr = list(map(int, input().split()))
    except EOFError:
        break

    idx = expr.index(-1)
    print(f"{calc[idx](*expr):.02f}")
