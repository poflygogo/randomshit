# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11475 Extend to Palindrome
# ZeroJudge e595


def extent_to_palindrome(text: str) -> str:
    j = len(text) - 1
    k = 0
    for i in range(len(text)):
        if text[i] == text[j]:
            j -= 1
        else:
            k = i + 1
    return text + ''.join(reversed(text[:k]))


def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        print(extent_to_palindrome(text))


if __name__ == '__main__':
    main()
