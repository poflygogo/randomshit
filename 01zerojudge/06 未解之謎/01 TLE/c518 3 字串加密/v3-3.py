# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c518. 3. 字串加密


n, m = map(int, input().split())
text = input()
code1 = input()
code2 = input()

trans_rule = {chr(i):{chr(i)} for i in range(ord('a'), ord('z') + 1)}
trans_rule.update({chr(i):{chr(i)} for i in range(ord('A'), ord('Z') + 1)})
trans_rule.update({chr(i):{chr(i)} for i in range(ord('0'), ord('9') + 1)})

for i in range(m):
    if code1[i] == code2[i] or not trans_rule[code1[i]]:
        continue
    trans_rule[code2[i]].update(trans_rule[code1[i]])
    trans_rule[code1[i]].clear()

trans = {}
for i in trans_rule:
    if trans_rule[i]:
        i_ord = ord(i)
        trans.update({ord(j): i_ord for j in trans_rule[i]})

print(text.translate(trans))
