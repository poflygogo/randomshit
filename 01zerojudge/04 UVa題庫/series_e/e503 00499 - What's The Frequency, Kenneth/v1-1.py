# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00499 What's The Frequency, Kenneth?
# ZeroJudge e503

while True:
    try:
        text = input().rstrip()
    
    except EOFError:
        exit()
    
    else:
        counter = {}
        for char in text:
            if char.isalpha():
                counter[char] = counter.get(char, 0) + 1
        
        max_value = max(counter.values())
        print(''.join(sorted(i for i in counter if counter[i] == max_value)), max_value)
