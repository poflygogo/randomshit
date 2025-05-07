# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c660. 墨西哥波浪舞


text = list(input().lower())
length = len(text)
i = 0
while i < length:
    while i < length and text[i] == ' ':
        i += 1
    text[i] = text[i].upper()
    print(''.join(text))
    text[i] = text[i].lower()
    i += 1
