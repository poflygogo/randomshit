from sys import stdin, stdout

_ = stdin.readline()
data:list = stdin.readlines()
data = [i.strip() for i in data]
key = tuple(map(int, data.pop(-2).split()))
data = ''.join(data)
result = [data[i - 1] for i in key]
stdout.write(f'{"".join(result)}\n')