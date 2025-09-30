# python 3.12
# UVa 10815 Andy’s First Dictionary
# ZeroJudge r366

from sys import stdin


def parser(s: str):
    i = 0
    while i < len(s):
        while i < len(s) and not s[i].isalpha():
            i += 1
        j = i + 1
        while j < len(s) and s[j].isalpha():
            j += 1
        yield s[i:j].lower()
        i = j + 1


def main():
    s = stdin.read()
    words = {i for i in parser(s)}
    if "" in words:
        words.remove("")
    print(*sorted(words), sep="\n")


main()
