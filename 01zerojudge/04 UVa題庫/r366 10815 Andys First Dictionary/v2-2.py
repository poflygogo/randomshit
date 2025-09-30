# python 3.12
# UVa 10815 Andy’s First Dictionary
# ZeroJudge r366

# ---------------------------------------------------

import sys
import io
Q = """
Adventures in Disneyland
Two blondes were going to Disneyland when they came to a fork in the
road. The sign read: "Disneyland Left."
So they went home.
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


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
    words = set()
    while True:
        try:
            words.update({i for i in parser(input())})
        except EOFError:
            break
    if "" in words:
        words.remove("")
    print(*sorted(words), sep='\n')


main()
