pie, man, score = map(int, input().split())
qualification = []
for i in range(pie):
    data = sorted(map(int, input().split()))
    if sum(data[1:-2]) / (man - 2) >= score:
        qualification.append(i + 1)

if qualification:
    print(*qualification, sep='\n')
else:
    print('A is for apple.')
