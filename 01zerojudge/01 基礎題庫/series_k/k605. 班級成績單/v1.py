students = [list(map(lambda x: int(x) if x.isdecimal() else x ,input().split())) for _ in range(int(input()))]
students.sort(key= lambda x: (-sum(x[2:]), x[0]))
score = [sum(line[2:]) for line in students]

for idx, stu in enumerate(students):
    print(
        *stu,
        score[idx],
        1 if idx == 0 else score.index(score[idx]) + 1 if score[idx] == score[idx - 1] else idx + 1
    )