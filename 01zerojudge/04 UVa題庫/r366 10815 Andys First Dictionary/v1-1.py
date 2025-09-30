# python 3.12
# UVa 10815 Andy’s First Dictionary
# ZeroJudge r366

from sys import stdin
import re

s = stdin.read().lower()
res = "\n".join(sorted(set(re.findall(r"[A-Za-z]+", s))))
print(res)
