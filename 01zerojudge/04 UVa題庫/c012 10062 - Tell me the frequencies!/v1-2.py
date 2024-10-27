from sys import stdin


for line in stdin:
    counter = {}
    for i in line.rstrip():
        i = ord(i)
        counter[i] = counter.get(i, 0) + 1

    for key in sorted(counter, key=lambda x: (counter[x], -x)):
        print(key, counter[key])
