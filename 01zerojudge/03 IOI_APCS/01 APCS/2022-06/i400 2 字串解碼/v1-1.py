# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i400. 2. 字串解碼
# 2022-06 APCS


def encrypt(n1: int, s: str, n2: int, e: str) -> str:
    """
    args:
        n1: length of s
        s: String to be encrypted
        n2: length of e
        e: encrypted rule string that included only 1 and 0
    return:
        str, a encrypted string
    """
    if e.count('1') & 1 != 0:
        if n1 & 1 != 0:
            s = s[n1 // 2 + 1:] + s[n1 // 2] + s[:n1 // 2]
        else:
            s = s[n1 // 2:] + s[:n1 // 2]
    result = []
    lft, rgt = 0, n1 - 1
    for char in e:
        if char == '1':
            result.append(s[rgt])
            rgt -= 1
        else:
            result.append(s[lft])
            lft += 1
    return ''.join(result)


def decrypt(n: int, s: list, e: str):
    result = []
    s = reversed(s)
    for char in reversed(e):
        if char == '1':
            result.append(next(s))
        else:
            result.insert(0, next(s))

    if e.count('1') & 1 != 0:
        if n & 1 != 0:
            result[:n // 2], result[n // 2 + 1:] = result[n // 2 + 1:], result[:n // 2]
        else:
            result[:n // 2], result[n // 2:] = result[n // 2:], result[:n // 2]

    return result


def main():
    m, n = map(int, input().split())
    data = [input() for _ in range(m)]
    text = list(input())
    for item in reversed(data):
        text = decrypt(n, text, item)
    print(''.join(text))


if __name__ == '__main__':
    main()
