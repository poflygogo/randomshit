# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00865 Substitution Cypher
# ZeroJudge e501


T = int(input())
input()

for _ in range(T):
    decode, encode = input().rstrip(), input().rstrip()
    key = dict(zip(decode, encode))

    print(encode, decode, sep='\n')
    while True:
        try:
            text_raw = input().rstrip()

        except EOFError:
            exit()

        else:
            if not text_raw:
                print()
                break

            print(*[key[char] if char in key else char for char in text_raw], sep='')
