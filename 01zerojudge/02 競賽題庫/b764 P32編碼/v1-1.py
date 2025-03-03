# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b764. P32編碼
# 101學年度商業類程式設計競賽正式題


from sys import stdin
scan = stdin.readline

decode = {
    '00': 'A',
    '01': 'B',
    '100': '0',
    '101': '1',
    '1100': '2',
    '1101': '3',
    '11100': '4',
    '11101': '5',
    '111100': '6',
    '111101': '7',
    '111110': '8',
    '111111': '9'
}

for n in stdin:
    for _ in range(int(n.rstrip())):
        code = scan().rstrip()
        s = 0
        result = []
        for i in range(2, len(code) + 1):
            if code[s:i] in decode:
                result.append(decode[code[s:i]])
                s = i
        result.insert(4, ',')
        print(''.join(result))
