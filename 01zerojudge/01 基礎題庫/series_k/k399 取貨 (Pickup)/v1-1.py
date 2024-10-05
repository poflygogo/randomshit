data = input()
employee = sorted(set(data))
total = len(employee)

order = {}
k = total
for i in data[::-1]:
    if i in order:
        continue

    order[i] = k
    k -= 1

    if k == 0:
        break

print(
    *[order[i] for i in employee],
    sep=''
)
