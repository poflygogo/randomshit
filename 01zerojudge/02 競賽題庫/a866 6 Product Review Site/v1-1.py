# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a866. 6. Product Review Site
# HP CodeWars 2010


data = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
while True:
    temp = input().rstrip()
    if temp == '0':
        break
    data[temp] += 1

for i in range(5, 0, -1):
    i = str(i)
    print(f'{i} ({str(data[i]):>2s}) |{"=" * data[i]}')

print(f'Average rating: {sum(int(i) * data[i] for i in data) / sum(data.values()):.4f}')
