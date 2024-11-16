# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11713 Abstract Names
# ZeroJudge e554


vowel = {'a', 'e', 'i', 'o', 'u'}
for _ in range(int(input())):
    name_real = input().rstrip()
    name_game = input().rstrip()

    flag = True
    if len(name_real) != len(name_game):
        flag = False
    
    else:
        for idx in range(len(name_real)):
            if name_real[idx] == name_game[idx]:
                continue

            if name_real[idx] not in vowel or name_game[idx] not in vowel:
                flag = False
                break
        
    print('Yes' if flag else 'No')
