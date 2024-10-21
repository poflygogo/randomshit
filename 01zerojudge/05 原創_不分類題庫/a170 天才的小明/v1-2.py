from sys import stdin, stdout


ans = []
for _ in range(int(stdin.readline().rstrip())):
    ans.append(hex(sum(map(lambda x: int(x, 8), stdin.readline().rstrip().split())))[2:].upper())
stdout.write('\n'.join(ans))

# zerojudge a170
# AC (2.7s, 79.2MB)
# 2024-10-22
