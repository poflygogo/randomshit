# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e786. b1.修辭迴文(Palindrome)
# 2019-12 TOI 練習賽


def is_palindrome(text):
    length = len(text)
    if length % 2 != 0:
        return 'NO'
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return 'NO'
    return 'YES\n' + text[:length // 2]


if __name__ == '__main__':
    text = input()
    print(is_palindrome(text))
