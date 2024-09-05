import sys

_ = input()
data = {}
for ele in sys.stdin:
    ele = int(ele)
    if ele in data:
        data[ele] += 1
    else:
        data[ele] = 1

for i in sorted(data.keys()):
    print(i, data[i])