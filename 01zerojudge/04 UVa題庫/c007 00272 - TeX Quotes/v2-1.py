from sys import stdin, stdout


data = stdin.read()
for _ in range(data.count('"') // 2):
    data = data.replace('"', '``', 1).replace('"', '\'\'', 1)

stdout.write(data)
