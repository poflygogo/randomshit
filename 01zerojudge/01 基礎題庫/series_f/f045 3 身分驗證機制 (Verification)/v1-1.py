idnum = input()
max1, max2 = 0, 0
for i in idnum:
    i = int(i)
    if i > max1:
        max1, max2 = i, max1
    elif i > max2:
        max2 = i
print(
    'Good Morning!' if int(idnum[-3:]) == max1 ** 2 + max2 ** 2
    else 'SPY!'
)
