# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00256 Quirksome Squares
# ZeroJudge d182

from sys import stdin, stdout


quicksome_number = {
    '2': '00\n01\n81\n',
    '4': '0000\n0001\n2025\n3025\n9801\n',
    '6': '000000\n000001\n088209\n494209\n998001\n',
    '8': '00000000\n00000001\n04941729\n07441984\n24502500\n25502500\n52881984\n60481729\n99980001\n'
}

for line in stdin:
    stdout.write(quicksome_number[line.rstrip()])

# shit solution lol
