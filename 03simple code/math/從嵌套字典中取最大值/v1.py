"""
有一群學生，將他們的各科成績用字典紀錄下來
找出總分最高的那位
"""
student = {
    "Andy":{"English":85,"Math":96,"Science":88},
    "John":{"English":72,"Math":80,"Science":91},
    "Alex":{"English":83,"Math":69,"Science":75}}

max_student = max(student, key=lambda x: sum(student[x].values()))
print("max_student")
