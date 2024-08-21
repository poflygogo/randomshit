"""
輸入三門課的成績
如果 分數<60 得0積分
如果 60<分數<90 得1積分
如果 分數>90 得2積分
求積分總和
"""
total = 0
for i in range(1, 4):
    score = int(input(f"請輸入第{i}門課成績: "))
    if score > 90: total += 2
    elif score > 60: total += 1
print(f"總積分為{total}")
