# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j245. 111北二4a.加密密文
# 111北二區桃竹苗資訊學科能力複賽


def encrypt(text: str) -> str:
    text1 = step1(text)
    text2 = step2(text1)
    h = step3(text1, text2)
    return ''.join(step4(text2, h))


def step1(text: str):
    result = list(text)
    mid = len(result) // 2
    result.append(result.pop(mid))
    if len(text) % 2 == 0:
        result.insert(0, result.pop(mid - 1))
    else:
        result.insert(0, result[-1])
    return result


def step2(text1: list):
    result = []
    lft, rgt = 0, len(text1) - 1
    for i in text1:
        if ord(i) % 2 == 0:
            result.append(text1[rgt])
            rgt -= 1
        else:
            result.append(text1[lft])
            lft += 1
    return result


def step3(text1: list, text2: list, r: int=4):
    result = [(ord(text1[i]) % 2 != 0) ^ (ord(text2[i]) % 2 != 0) for i in range(r)]
    return sum(result)


def step4(text2: list, h: int):
    return [chr(ord(i) + h) for i in text2]


if __name__ == '__main__':
    text = input()
    print(encrypt(text))
