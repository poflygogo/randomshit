from sys import stdin, stdout

length = int(stdin.readline())
people = tuple(map(int, stdin.readline().split()))

result = []
for idx, item in enumerate(people):
    if idx == 0:
        result.append(0)
        continue

    for jdx, jtem in enumerate(people[idx-1::-1]):
        if jtem < item:
            result.append(idx - jdx)
            break
    else:
        result.append(0)

result = ' '.join(map(str, result))
stdout.write(result)