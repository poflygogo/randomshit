def type_sum(n):
    return sum([len(data[n][i]) for i in data[n]])

def class_sum(n):
    return sum([len(data[i][n]) for i in data])

# 第一層代表軍種、第二層代表軍階，第三層代表姓名
data = {
    '1': {
        '1': set(),
        '2': set(),
        '3': set()
    },
    '2': {
        '1': set(),
        '2': set(),
        '3': set()
    },
    '3': {
        '1': set(),
        '2': set(),
        '3': set()
    }
}

mans, back = map(int, input().split())
for _ in range(back):
    name, mtype, mclass = input().split()
    data[mtype][mclass].add(name)

surv_rate = sum([len(data[i][j]) for i in data for j in data]) / mans * 100

print(
    f"navy:{type_sum('1')} army:{type_sum('2')} air:{type_sum('3')}",
    f"officer:{class_sum('1')} sergeant:{class_sum('2')} soldier:{class_sum('3')}",
    f'survival rate:{surv_rate : .1f}%',
    sep='\n'
)