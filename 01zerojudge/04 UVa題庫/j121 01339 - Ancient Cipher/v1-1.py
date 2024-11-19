# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01339 Ancient Cipher
# ZeroJudge j121

# 不需要真的去解碼，只需要檢查元素重複的頻率是否相同即可


while True:
    try:
        encode = input().rstrip()
        decode = input().rstrip()
    
    except EOFError:
        exit()
    
    else:
        encode_element = {}
        for i in encode:
            encode_element[i] = encode_element.get(i, 0) + 1
        
        decode_element = {}
        for i in decode:
            decode_element[i] = decode_element.get(i, 0) + 1
        
        if sorted(encode_element.values()) == sorted(decode_element.values()):
            print('YES')
        
        else:
            print('NO')
