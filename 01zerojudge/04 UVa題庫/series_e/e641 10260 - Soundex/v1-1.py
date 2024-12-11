# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10260 Soundex
# ZeroJudge e641


Soundex_code = {
    'B': '1', 'F': '1', 'P': '1', 'V': '1',
    'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}

while True:
    try:
        text = input()
    except EOFError:
        break
    else:
        result = [Soundex_code.get(text[0], '')]
        for i in range(1, len(text)):
            if Soundex_code.get(text[i], '') != Soundex_code.get(text[i - 1], ''):
                result.append(Soundex_code.get(text[i], ''))
        print(''.join(result))
