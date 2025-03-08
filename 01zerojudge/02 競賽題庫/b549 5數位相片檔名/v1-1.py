# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b549. 5.數位相片檔名


# ---------------------------------------------------

import sys
import io
Q = """
10 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 4 A 6 
14 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 4 A 6 D 3 A 7 D 0 A 8 
14 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 5 A 6 A 7 D 0 A 8 A 9 
14 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 5 A 6 A 7 A 8 D 4 A 9 
15 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 5 A 6 A 7 A 8 D 4 A 9 A 10 
17 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 5 A 6 A 7 A 8 D 4 A 9 A 10 D 6 A 11
19 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 D 5 A 6 A 7 A 8 D 4 A 9 A 10 D 6 A 11 D 11 A 12
9 A 0 A 1 A 2 A 3 D 2 A 4 D 1 D 0 A 5
9 A 0 A 1 A 2 A 3 D 2 A 4 D 1 A 5 A 6
10 A 0 A 1 A 2 A 3 A 4 D 2 A 5 A 6 D 3 A 7
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


def main():
    result = []
    while True:
        try:
            n, *commands = input().split()
        except EOFError:
            break
        result.append(photo_file_name(int(n), commands))
    print('\n--\n'.join(result))


def photo_file_name(n: int, commands: list) -> str:
    available_nums = set(range(1000))
    photos_info = {}    # (time, id)
    for i in range(0, n*2, 2):
        if commands[i] == 'A':
            add_file(available_nums, photos_info, int(commands[i+1]))
        else:           # commands == 'D'
            del_file(available_nums, photos_info, int(commands[i+1]))
    result = [photos_info.popitem()[1] for _ in range(2)]
    return '\n'.join(f'PIC{i:03d}' for i in reversed(result))
            

def add_file(nums: set, data: dict, time: int):
    for i in range(1000):
        if i in nums and is_valid(data, time, i):
            data[time] = i
            nums.remove(i)
            return


def del_file(nums: set, data: dict, time: int):
    for i in data:
        if i == time:
            nums.add(data.pop(i))
            return


def is_valid(data: dict, time: int, target: int) -> bool:
    data[time] = target
    flag = True
    arr1 = []
    arr2 = []
    for i in sorted(data):
        if not arr1 or arr1[-1] < data[i]:
            arr1.append(data[i])
        elif not arr2 or arr2[-1] < data[i]:
            arr2.append(data[i])
        else:
            flag = False
            break
    data.pop(time)
    return flag


if __name__ == '__main__':
    main()
