# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c518. 3. 字串加密


n, m = map(int, input().split())
text = input()
code1 = input()
code2 = input()

dictionary = {i:i for i in range(ord('a'), ord('z') + 1)}
dictionary.update({i:i for i in range(ord('A'), ord('Z') + 1)})
dictionary.update({i:i for i in range(ord('0'), ord('9') + 1)})

for i in range(len(code1)):
    a, b = ord(code1[i]), ord(code2[i])
    for key in dictionary:
        if dictionary[key] == a:
            dictionary[key] = b

print(text.translate(dictionary))
