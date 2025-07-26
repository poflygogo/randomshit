# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e640. 造句


SUCCEED = "對"
FAIL = "錯"


def pattern_analyzer(s: str):
    last = 0
    while last < len(s):
        idx = s.find("...", last)
        if idx == 0:
            yield None
        elif idx == -1:
            yield s[last:]
        else:
            yield s[last:idx]
            yield None
        last = idx + 3


def is_valid(prompt: str, s: str):
    last = 0
    for item in pattern_analyzer(prompt):
        if item is None:
            last += 1
        else:
            idx = s.find(item, last)
            if idx == -1 or (last == 0 < idx):
                return False
            last = idx + len(item)
    if prompt[-1] is None and last >= len(s):
        return False
    return True


def main():
    for i in range(1, int(input()) + 1):
        input()
        prompt = input()
        if i > 1:
            print()
        print(f"第{i}題:")
        for _ in range(int(input())):
            if is_valid(prompt, input()):
                print(SUCCEED)
            else:
                print(FAIL)


if __name__ == "__main__":
    main()
