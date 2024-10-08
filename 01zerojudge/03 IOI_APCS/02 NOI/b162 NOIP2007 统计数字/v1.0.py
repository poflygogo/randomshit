import sys, collections

data = [int(i) for i in sys.stdin]
data_count = collections.Counter(data)
for ele in sorted(data_count.keys()):
    print(ele, data_count[ele])