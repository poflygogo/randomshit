# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c518. 3. 字串加密


n, m = map(int, input().split())
text = input()
code1 = input()
code2 = input()

trans_rule = {i:{i} for i in range(ord('a'), ord('z') + 1)}
trans_rule.update({i:{i} for i in range(ord('A'), ord('Z') + 1)})
trans_rule.update({i:{i} for i in range(ord('0'), ord('9') + 1)})

for i in range(m):
    a, b = ord(code1[i]), ord(code2[i])
    if a == b or not trans_rule[a]:
        continue
    trans_rule[b].update(trans_rule[a])
    trans_rule[a].clear()

trans = {}
for i in trans_rule:
    if trans_rule[i]:
        trans.update({j: i for j in trans_rule[i]})

print(text.translate(trans))
