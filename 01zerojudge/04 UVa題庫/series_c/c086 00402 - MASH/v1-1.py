# python 3.12
# UVa 402 M*A*S*H
# ZeroJudge c086


def solve(n: int, x: int, cards: list) -> list:
    arr = list(range(1, n + 1))
    for val in cards:
        if len(arr) <= x:
            break
        tmp = arr[val - 1 :: val]
        del arr[val - 1 :: val]

    if (t := len(arr)) < x:
        tmp.reverse()
        arr.extend(tmp[: x - t])
        arr.sort()

    return arr


def main():
    test_case = 1
    while True:
        try:
            n, x, *cards = map(int, input().split())
            if test_case > 1:
                print()
            print(f"Selection #{test_case}")
            print(*solve(n, x, cards))
            test_case += 1
        except EOFError:
            break


main()
