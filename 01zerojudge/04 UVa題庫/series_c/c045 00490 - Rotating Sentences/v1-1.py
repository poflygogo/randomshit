from sys import stdin
# stdin = open('test_case.txt')


data = [line.rstrip() for line in stdin]
data.reverse()
max_length = max(map(len, data))
for i in range(max_length):
    print(''.join(line[i] if len(line) > i else ' ' for line in data))
