# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b867. Jason


import json
from sys import stdin

scan = stdin.readline


def read_data(root: dict, obj: dict):
    command = scan().rstrip().split()
    while command[0] != 'end':
        if command[2] == 'newJSONObject':
            obj[command[1].strip('"')] = {}
            read_data(obj[command[1].strip('"')], {})
        else:
            obj[command[1].strip('"')] = command[2].strip('"')
        command = scan().rstrip().split()
    root.update(obj)


def main():
    result = {}
    read_data(result, {})
    print(json.dumps(result, separators=(',', ':')))


if __name__ == '__main__':
    main()
