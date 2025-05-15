# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b428. 凱薩加密


while True:
    try:
        text1 = input()
        text2 = input()
    except EOFError:
        break
    print((26 + ord(text2[0]) - ord(text1[0])) % 26)
