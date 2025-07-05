# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e570. 賓語提前


while True:
    try:
        s = input()
        if "之" in s:
            s1, s2 = s.split("之")
        else:
            s1, s2 = s.split("是")
        print(s2 + s1)
    except EOFError:
        break
