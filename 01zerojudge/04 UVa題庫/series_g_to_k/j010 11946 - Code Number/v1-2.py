# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11946 Code Number
# ZeroJudge j010


code_message = ("H3LL0 MY L0V3, 1 M H499Y 83C4U53 500N 1 W1LL 83 70 Y0UR 51D3.\n"
                "7H15 71M3 W17H0U7 Y0U H45 833N 373RN4L. 1 1NV173 Y0U 70 7H3 200\n"
                "0N3 70 533 7H3 238R42 4ND 60R1L45.\n")
decode_message = ("HELLO MY LOVE, I M HAPPY BECAUSE SOON I WILL BE TO YOUR SIDE.\n"
                  "THIS TIME WITHOUT YOU HAS BEEN ETERNAL. I INVITE YOU TO THE ZOO\n"
                  "ONE TO SEE THE ZEBRAS AND GORILAS.\n")
trans_table = str.maketrans(code_message, decode_message)
trans_table[ord('2')] = ord('Z')
trans_table[ord('5')] = ord('S')

for i in range(int(input())):
    try:
        text = input()
        if i != 0:
            print()
        while text:
            print(text.translate(trans_table))
            text = input()
    except EOFError:
        break
