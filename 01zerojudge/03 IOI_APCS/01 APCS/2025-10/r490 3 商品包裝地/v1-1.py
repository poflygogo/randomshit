# python 3.12
# ZeroJudge r490. 3. 商品包裝地
# APCS 2025-10

# ---------------------------------------------------

import sys
import io

Q = """
4
4710018000102
0309876543216
4711234560012
3001111111118
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


def is_valid(code: str) -> bool:
    return (sum(map(int, code[:-1:2])) + 3 * sum(map(int, code[1:-1:2]))) % 10 + int(
        code[-1]
    ) in (0, 10)


def main():
    counter = {}
    for _ in range(int(input())):
        code = input().strip()
        if is_valid(code):
            t = code[:3]
            counter[t] = counter.get(t, 0) + 1
    print(*max(counter.items(), key=lambda x: x[1]))


main()
