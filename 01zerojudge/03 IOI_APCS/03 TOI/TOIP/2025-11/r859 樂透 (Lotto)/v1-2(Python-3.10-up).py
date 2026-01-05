# ZeroJudge r859
# TOI 練習賽 新手組 第二題 樂透 (Lotto)
# python 3.12


def main():
    guess = set(map(int, input().split()))
    target = list(map(int, input().split()))
    special = target.pop()
    target = set(target)

    total_match = len(guess.intersection(target))
    match_special = special in guess

    match [total_match, match_special]:
        case [6, _]:
            print("A")
        case [5, True]:
            print("B")
        case [5, False]:
            print("C")
        case [4, True]:
            print("D")
        case [4, False]:
            print("E")
        case [3, True]:
            print("F")
        case [2, True]:
            print("G")
        case [3, False]:
            print("H")
        case _:
            print("X")


main()
