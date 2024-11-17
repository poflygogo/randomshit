# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f281. 志樺的亮度


stu_total = int(input())
stu_member = list(map(int, input().split()))
light = int(input())

zhi_hua = min(stu_member)
stu_member.remove(zhi_hua)

diff = light - zhi_hua

print(diff if min(stu_member) - diff >= light else 'You are too black!')
    