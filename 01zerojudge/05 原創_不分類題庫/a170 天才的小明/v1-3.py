from sys import stdin, stdout


data = stdin.readlines()
del data[0]
stdout.writelines([
    hex(sum(map(lambda x: int(x, 8), line.rstrip().split())))[2:].upper() + '\n' for line in data
])

# zerojudge a170
# AC (2.5s, 175.2MB)
# 2024-10-22
