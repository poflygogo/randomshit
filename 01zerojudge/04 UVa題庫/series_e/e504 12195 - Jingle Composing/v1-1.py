# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12195 Jingle Composing
# ZeroJudge e504

symbol = {
    'W': 64, 'H': 32, 'Q': 16, 'E': 8,
    'S': 4, 'T': 2, 'X': 1
}

while True:
    data = input().rstrip()
    if data == '*':
        exit()
    
    data = data.strip('/').split('/')
    print(sum(64 == sum(symbol[i] for i in bar) for bar in data))
