# -*- encoding: utf-8 -**-
# python 3.12
# UVa 458 The Decoder
# ZeroJudge f434


translator = {i:i - 7 for i in range(39, 127)}
while True:
    try:
        text = input()
    except EOFError:
        break
    else:
        print(text.translate(translator))
