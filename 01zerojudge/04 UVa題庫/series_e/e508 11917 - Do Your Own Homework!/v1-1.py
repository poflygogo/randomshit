# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11917 Do Your Own Homework!
# ZeroJudge e508

for case in range(1, int(input()) + 1):
    ability = dict([input().split() for _ in range(int(input()))])

    time = int(input())
    subject = input()

    if subject not in ability:
        result = 'Do your own homework!'
    
    elif time >= int(ability[subject]):
        result = 'Yesss'
    
    elif time + 5 >= int(ability[subject]):
        result = 'Late'
    
    else:
        result = 'Do your own homework!'
    
    print(f'Case {case}: {result}')
