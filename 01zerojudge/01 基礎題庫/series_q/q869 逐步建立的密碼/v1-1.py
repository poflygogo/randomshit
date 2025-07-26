# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q869. 逐步建立的密碼


foo = [input() for _ in range(int(input()))]
foo.sort(key=lambda x: (len(x), x))

width = len(foo[-1])
print('\n'.join(i.rjust(width) for i in foo))
