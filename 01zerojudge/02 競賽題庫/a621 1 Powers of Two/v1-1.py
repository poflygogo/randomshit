# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a621. 1. Powers of Two
# HP CodeWars 2007


print(*[f'2^{i} = {2 ** i}' for i in range(int(input()) + 1)], sep='\n')
