# -*- encoding: utf-8 -**-
# python 3.12
# UVa 458 The Decoder
# ZeroJudge f434


import sys


table = str.maketrans({i:i - 7 for i in range(39, 127)})
sys.stdout.write(sys.stdin.read().translate(table))
