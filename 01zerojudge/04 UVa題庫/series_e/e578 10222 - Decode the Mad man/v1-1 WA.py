# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10222 Decode the Mad man
# ZeroJudge e578


translator = dict(zip("ertyuiop[]dfghjkl;'cvbnm,./", "qwertyuiopasdfghjklzxcvbnm"))

while True:
    try:
        print(''.join(translator[i] if i in translator else i for i in input()))
    except EOFError:
        break
