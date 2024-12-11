# -*- encoding: utf-8 -**-
# python 3.12
# UVa 458 The Decoder
# ZeroJudge f434


while True:
    try:
        text = input()
    except EOFError:
        break
    else:
        print(''.join(chr(ord(i) - 7) for i in text))
