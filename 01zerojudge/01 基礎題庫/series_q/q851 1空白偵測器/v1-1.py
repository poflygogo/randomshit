# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q851. 1.空白偵測器


def space_detector(text: str) -> str:
    result = list(text)
    k = None
    for i in range(len(text)):
        if text[i] != ' ':
            if k is not None and (i - k) > 1:
                result[k:i - 1] = ['*'] * (i - k - 1)
            elif k == 0 and i == 1:
                result[k] = '*'
            k = None
        elif k is None:
            k = i
    if k:
        result[k:] = ['*'] * (len(text) - k)
    return ''.join(result)


while True:
    try:
        print(space_detector(input()))
    except EOFError:
        break
