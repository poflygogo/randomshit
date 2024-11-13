# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11764 Jumping Mario
# ZeroJudge d660

for case in range(1, int(input()) + 1):
    walls_total = int(input())
    walls = list(map(int, input().split()))

    if walls_total <= 1:
        print(f'Case {case}: 0 0')
        continue

    high_jump_times, low_jump_times = 0, 0
    current_wall = walls[0]

    for wall in walls[1:]:
        if wall > current_wall:
            high_jump_times += 1
        elif wall < current_wall:
            low_jump_times += 1
        
        current_wall = wall
    
    print(f'Case {case}: {high_jump_times} {low_jump_times}')
