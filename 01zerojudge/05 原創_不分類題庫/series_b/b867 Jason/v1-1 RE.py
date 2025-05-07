# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b867. Jason


import json
from sys import stdin

scan = stdin.readline


def read_data(root: dict, obj: dict):
    command = scan().rstrip().split()
    if command[0] == 'end':
        root.update(obj)
        return
    if command[2] == 'newJSONObject':
        obj[command[1].strip('"')] = {}
        read_data(obj[command[1].strip('"')], {})
    else:
        obj[command[1].strip('"')] = command[2].strip('"')
    read_data(root, obj)


def main():
    result = {}
    read_data(result, {})
    print(json.dumps(result, separators=(',', ':')))


if __name__ == '__main__':
    main()
