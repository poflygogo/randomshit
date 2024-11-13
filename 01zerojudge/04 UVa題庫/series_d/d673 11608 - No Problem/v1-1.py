# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11608 No Problem
# ZeroJudge d673

case = 0
while True:
    problem_total = int(input())
    if problem_total < 0:
        exit()
    
    case += 1
    print(f'Case {case}:')

    problem_get = tuple(map(int, input().split()))
    problem_need = tuple(map(int, input().split()))

    for idx in range(12):
        if problem_need[idx] <= problem_total:
            print('No problem! :D')
            problem_total -= problem_need[idx]
        
        else:
            print('No problem. :(')
        
        problem_total += problem_get[idx]
