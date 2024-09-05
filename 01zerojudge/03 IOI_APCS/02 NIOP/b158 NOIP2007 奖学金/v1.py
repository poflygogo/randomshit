data = {}
for stu in range(1, int(input()) + 1):
    data[stu] = {}
    data[stu]['score'] = tuple(map(int, input().split()))
    data[stu]['total'] = sum(data[stu]['score'])

students = list(data.keys())
students.sort(key= lambda x: (data[x]['total'], data[x]['score'][0], x * -1))
for i in range(5):
    stu = students.pop()
    print(stu, data[stu]['total'])