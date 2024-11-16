# -*- encoding: utf-8 -*-
# python 3.12
# UVa e516. 10409 - Die Game
# ZeroJudge e516


while True:
    total_command = int(input().rstrip())
    if not total_command:
        exit()
    
    dice_top = 1
    dice_north = 2
    dice_west = 3
    for _ in range(total_command):
        command = input().rstrip()
        if command == 'north':
            dice_top, dice_north = 7 - dice_north, dice_top

        elif command == 'east':
            dice_top, dice_west = dice_west, 7 - dice_top

        elif command == 'south':
            dice_top, dice_north = dice_north, 7 - dice_top

        else:   # command == 'west'
            dice_top, dice_west = 7 - dice_west, dice_top
        
    print(dice_top)
