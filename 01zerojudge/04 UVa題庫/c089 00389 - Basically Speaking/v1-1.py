from sys import stdin


for line in stdin:
    line = line.rstrip().split()
    if line[0] == '0':
        print('      0')
        continue

    n = int(line[0], int(line[1]))
    base = int(line[2])

    ans = []
    while n > base:
        ans.append(n % base)
        n //= base
    ans.append(n)
    ans.reverse()
    ans = ''.join(str(i) if i < 9 else 'ABCDEF'[i - 10] for i in ans)

    if len(ans) > 7:
        print('  ERROR')
    else:
        print(f'{ans:>7s}')
