# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10282 Babelfish
# ZeroJudge n764


from sys import stdin

my_dict = {}
for line in stdin:
    if not line.rstrip():
        break
    a, b = line.rstrip().split()
    my_dict[b] = a

for line in stdin:
    print(my_dict.get(line.rstrip(), 'eh'))
