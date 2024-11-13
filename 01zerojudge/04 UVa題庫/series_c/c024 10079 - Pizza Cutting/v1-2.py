from sys import stdin


data = [int(i) * (int(i) + 1) // 2 + 1 for i in stdin.readlines()[:-1]]
print(*data, sep='\n')
