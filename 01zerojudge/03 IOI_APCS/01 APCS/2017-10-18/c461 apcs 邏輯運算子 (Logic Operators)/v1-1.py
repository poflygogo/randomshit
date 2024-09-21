a, b, check = map(lambda x: bool(int(x)), input().split())
result = []
if (a & b) == check: result.append('AND')
if (a | b) == check: result.append('OR')
if (a ^ b) == check: result.append('XOR')

if result:
    print(*result, sep='\n')
else:
    print('IMPOSSIBLE')
