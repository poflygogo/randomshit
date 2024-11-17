# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f281. 志樺的亮度


stu_total = int(input())
stu_member = list(map(int, input().split()))
light = int(input())

stu_member.sort(reverse=True)
diff = light - stu_member.pop()

print(diff if stu_member.pop() - diff >= light else 'You are too black!')
    