a, b, check = map(lambda x: bool(int(x)), input().split())
result = []
if (a and b) == check: result.append('AND')
if (a or b) == check: result.append('OR')
if (a != b) == check: result.append('XOR')

if result:
    print(*result, sep='\n')
else:
    print('IMPOSSIBLE')
