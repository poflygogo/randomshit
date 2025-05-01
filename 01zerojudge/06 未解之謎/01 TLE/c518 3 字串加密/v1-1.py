# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c518. 3. 字串加密


n, m = map(int, input().split())
text = input()
code1 = input()
code2 = input()
for i in range(m):
    if code1[i] == code2[i]:
        continue
    text = text.replace(code1[i], code2[i])
print(text)
