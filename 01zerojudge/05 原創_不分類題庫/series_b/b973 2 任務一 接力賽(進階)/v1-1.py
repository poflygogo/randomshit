# ZeroJudge b973. 2.任務一->接力賽(進階)
# https://zerojudge.tw/ShowProblem?problemid=b973


def to_sce(s: str) -> int:
    # s should be "min:sec", eg: "12:05"
    min, sec = map(int, s.split(":"))
    return 60 * min + sec


while True:
    try:
        n, t = map(int, input().split())
        result = [0] * t
        for _ in range(n):
            times = [to_sce(i) for i in input().split()]
            for i in range(t):
                result[i] += times[i]
        result = sorted(enumerate(result, start=1), key=lambda x: (x[1], x[0]))
        print("\n".join(f"{i} {j}" for i, j in result))
    except EOFError:
        break
