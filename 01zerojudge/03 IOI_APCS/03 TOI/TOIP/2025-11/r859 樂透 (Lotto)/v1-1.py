# ZeroJudge r859
# TOI 練習賽 新手組 第二題 樂透 (Lotto)
# python 3.8


def main():
    guess = set(map(int, input().split()))
    target = list(map(int, input().split()))
    special = target.pop()
    target = set(target)

    total_match = len(guess.intersection(target))
    match_special = special in guess

    if total_match == 6:
        print("A")
    elif total_match == 5:
        print("B" if match_special else "C")
    elif total_match == 4:
        print("D" if match_special else "E")
    elif total_match == 3:
        print("F" if match_special else "H")
    elif total_match == 2 and match_special:
        print("G")
    else:
        print("X")


main()
