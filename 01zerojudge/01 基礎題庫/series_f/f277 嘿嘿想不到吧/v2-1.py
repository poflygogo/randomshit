# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f277. 嘿嘿想不到吧
# sort algorithm, custom sort


def main():
    data = [convert_to_tuple(input()) for _ in range(int(input()))]
    data.sort()
    for line in data:
        print(f'{line[0]} {line[1]} {line[2]}\n{line[3]}')


def convert_to_tuple(line: str):
    name, classroom, id, intro = line.split()
    return (int(classroom), int(id), name, intro) 


main()
 