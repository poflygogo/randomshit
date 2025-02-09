# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00417 Word Index
# ZeroJudge c077


from sys import stdin

nums = [chr(i) for i in range(97, 123)]     # 97 = ord('a'), 123 = ord('z') + 1
nums.extend([
    chr(i) + chr(j)
    for i in range(97, 123)
    for j in range(i + 1, 123)
])
nums.extend([
    chr(i) + chr(j) + chr(k)
    for i in range(97, 123)
    for j in range(i + 1, 123)
    for k in range(j + 1, 123)
])
nums.extend([
    chr(i) + chr(j) + chr(k) + chr(n)
    for i in range(97, 123)
    for j in range(i + 1, 123)
    for k in range(j + 1, 123)
    for n in range(k + 1, 123)
])
nums.extend([
    chr(i) + chr(j) + chr(k) + chr(n) + chr(m)
    for i in range(97, 123)
    for j in range(i + 1, 123)
    for k in range(j + 1, 123)
    for n in range(k + 1, 123)
    for m in range(n + 1, 123)
])
nums = {nums[i]: i + 1 for i in range(len(nums))}

for text in stdin:
    print(nums.get(text.rstrip(), '0'))
