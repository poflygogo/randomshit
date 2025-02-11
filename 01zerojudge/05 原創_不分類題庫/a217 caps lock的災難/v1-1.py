# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a217. caps lock的災難


from sys import stdin

for line in stdin:
    flag = True
    line = list(line)
    for i in range(len(line)):
        if not line[i].isalpha():
            if line[i] in {'!', '.', '?'}:
                flag = True
        elif flag:
            line[i] = line[i].upper()
            flag = False
        elif line[i] == 'i' and (not line[i - 1].isalpha() and not line[i + 1].isalpha()):
            line[i] = line[i].upper()
    print(''.join(line), end='')
