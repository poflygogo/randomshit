soldier = input().split()

for i in range(3):
    for j in range(len(soldier)):
        if j % 3 == i:
            print(soldier[j], end=' ')
    print()