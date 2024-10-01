a, b, c, d = map(int, input().rstrip().split())
print(f'{pow(a, b, pow(c, d)): <3,}'.replace(',', ' '))
