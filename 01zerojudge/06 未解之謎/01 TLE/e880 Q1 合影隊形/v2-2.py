# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e880. Q1 合影隊形
# 100學年度台北高中電腦程式設計競賽 


# ---------------------------------------------------

import sys
import io
Q = """
5 
2 
A B 
C D
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
    result = find_possible_line(info_dict, n, ascii_uppercase[:n], [], set())
    print(result if result else "No Solution")


def make_dict(info: list):
    result = defaultdict(set)
    for i in range(0, len(info), 2):
        result[info[i]].add(info[i + 1])
        result[info[i + 1]].add(info[i])
    return result


def find_possible_line(info: dict, n: int, token: str, path: list, seen: set):
    if len(path) == n:
        return ''.join(path)
    
    for i in token:
        if i not in seen and (not path or path[-1] not in info.get(i, set())):
            path.append(i)
            seen.add(i)
            result = find_possible_line(info, n, token, path, seen)
            if result:
                return result
            path.pop()
            seen.remove(i)
    return False


main()
