pie, man, score = map(int, input().split())
qualification = []
for i in range(pie):
    data = sorted(map(int, input().split()))
    del data[0], data[-1]
    if sum(data) / (man - 2) >= score:
        qualification.append(i)

if qualification:
    print(*qualification, sep='\n')
else:
    print('A is for apple.')
