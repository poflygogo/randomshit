pie, man, score = map(int, input().split())
qualification = []
for i in range(pie):
    data = [int(i) for i in input().split()]
    data.remove(max(data))
    data.remove(min(data))
    if sum(data) / (man - 2) >= score:
        qualification.append(i)

if qualification:
    print(*qualification, sep='\n')
else:
    print('A is for apple.')
