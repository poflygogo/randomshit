from sys import stdin


for line in stdin:
    print(
        int(line.rstrip()) ** 2 // 16
    )
