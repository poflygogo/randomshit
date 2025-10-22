# python 3.8
# ZeroJudge h206. 強者就是要戰，但......什麼才是強者呢？


def solve(arr: list, flag: bool = True):
    size = len(arr)
    if size == 1:
        return arr[0]
    elif flag:
        return max(solve(arr[: size // 2], False), solve(arr[size // 2 :], False))
    else:
        return min(solve(arr[: size // 2], True), solve(arr[size // 2 :], True))


def main():
    input()
    arr = list(map(int, input().split()))
    print(solve(arr))


main()
