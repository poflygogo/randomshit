location = input().split()
for i in ('A', 'K', 'k'):
    if i not in location:
        print(0)
        exit()

if 0 < location.index('K') - location.index('A') <= 2 and location.index('k') - location.index('K') == 1:
    print('星爆')
else:
    print(0)

# zerojudge o685
# 題目未公開
# AC (29ms, 3.3MB)
# 2024-10-22
