from itertools import zip_longest


def grouper(iterable, n=3, fillvalue=""):
    iterator = [iter(iterable)] * n
    return zip_longest(*iterator, fillvalue=fillvalue)


def solve(text: str) -> int:
    res = 0
    for i, j in enumerate(grouper(text)):
        if i % 2 == 0:
            res += int("".join(j))
        else:
            res += int("".join(reversed(j)))
    return res % 997


def main():
    while True:
        try:
            text = input()
            print(solve(text))
        except EOFError:
            break


main()
