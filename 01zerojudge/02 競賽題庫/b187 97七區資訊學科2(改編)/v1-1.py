# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b187. 97七區資訊學科2(改編)


from sys import stdin

print('十六進位表示法  相對應的十進位表示法')
for n in stdin:
    print(' ' * 6 + n.rstrip() + ' ' * 17 + str(int(n.rstrip(), 16)))
