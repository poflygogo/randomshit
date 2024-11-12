# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11577 Letter Frequency
# ZeroJudge d267

for _ in range(int(input())):
    counter = {}
    for char in input().rstrip().lower():
        if 97 <= ord(char) <= 122:
            counter[char] = counter.get(char, 0) + 1
    
    max_count = max(counter.values())
    print(*sorted([i for i in counter if counter[i] == max_count]), sep='')
    