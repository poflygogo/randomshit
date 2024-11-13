# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11220 Decoding the message
# ZeroJudge e269

cases = int(input())
input()

for case in range(1, cases + 1):
    print(f'Case #{case}:')
    while True:
        try:
            text_raw = input().rstrip().split()

        except EOFError:
            exit()

        else:
            if not text_raw:
                break

            idx = 0
            result = []
            for word in text_raw:
                if len(word) < idx + 1:
                    continue

                result.append(word[idx])
                idx += 1
            
            print(*result, sep='')
