# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00401 Palindromes
# ZeroJudge e543


# 數字 0 和字母 O 被視為相同字符，只有字母 O 是有效字符
mirror = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L',
    'L': 'J', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
    'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z',
    '8': '8'
}

while True:
    try:
        text = input().rstrip()

    except EOFError:
        exit()

    else:
        flag_is_mirror = True
        flag_is_palindrome = True

        if text != text[::-1]:
            flag_is_palindrome = False
        
        for idx in range(len(text) // 2 + 1):
            if text[idx] not in mirror or mirror[text[idx]] != text[-idx - 1]:
                flag_is_mirror = False
        
        print(
            f'{text} -- is',
            'a mirrored palindrome.' if flag_is_mirror and flag_is_palindrome else
            'a mirrored string.' if flag_is_mirror and not flag_is_palindrome else
            'a regular palindrome.' if not flag_is_mirror and flag_is_palindrome else
            'not a palindrome.'
        )
