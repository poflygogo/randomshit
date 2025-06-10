# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e880. Q1 合影隊形
# 100學年度台北高中電腦程式設計競賽 


# ---------------------------------------------------

import sys
import io
Q = """
4 
4 
A B 
C D 
C A 
C B
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



from sys import stdin
from string import ascii_uppercase
from collections import defaultdict


def main():
    n, _, *info = stdin.read().split()
    n = int(n)
    info_dict = make_dict(info)
    result = find_possible_line(info_dict, ascii_uppercase[:n], [])
    print(result if result else "No Solution")


def make_dict(info: list):
    result = defaultdict(set)
    for i in range(0, len(info), 2):
        result[info[i]].add(info[i + 1])
        result[info[i + 1]].add(info[i])
    return result


def find_possible_line(info: dict, token: str, path: list):
    if len(path) == len(token):
        return ''.join(path)
    
    for i in token:
        if not path:
            path.append(i)
            result = find_possible_line(info, token, path)
            if result:
                return result
            path.pop()
            continue
        if i not in path and path[-1] not in info[i]:
            path.append(i)
            result = find_possible_line(info, token, path)
            if result:
                return result
            path.pop()
    return False


main()
