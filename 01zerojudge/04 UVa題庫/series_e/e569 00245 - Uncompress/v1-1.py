# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00245 - Uncompress
# ZeroJudge e569


from re import findall


words = []
while True:
    text = input()                      # type: str
    if text == '0':
        break

    text = findall(r'\w+|\W+', text)    # type: list[str]
    for i in range(len(text)):
        if text[i].isdigit():
            idx = -int(text[i])
            text[i] = words[idx]
            words.append(words.pop(idx))
        elif text[i].isalpha():
            words.append(text[i])

    print(''.join(text))
