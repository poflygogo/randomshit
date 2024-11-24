# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a785. 7. It's All Greek To Me
# HP CodeWars 2008


key = (
    ('a', 'e', 'o'),
    ('a', 'e', 'i', 'y', 'o', 'ou', 'w')
)

val = (
    ('a', 'a', 'ai', 'a', 'w', 'w', 'w'),
    ('y', 'ei', 'ei', 'y', 'ou', 'ou', 'w'),
    ('w', 'ou', 'oi', 'w', 'ou', 'ou', 'w')
)

while True:
    text = input().rstrip()
    if text == 'END':
        break

    text = text.split('-')
    root = key[0].index(text[0][-1])

    if text[1][0] != 'o' or text[1][:2] != 'ou':
        suffix = key[1].index(text[1][0])
        print(text[0][:-1] + val[root][suffix] + text[1][1:])
    else:
        suffix = 5
        print(text[0][:-1] + val[root][suffix] + text[1][2:])
