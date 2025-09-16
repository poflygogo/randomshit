# ZeroJudge b972. 1.任務一->接力賽
# https://zerojudge.tw/ShowProblem?problemid=b972


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
        result.sort()
        print(*result, sep='\n')
    except EOFError:
        break
