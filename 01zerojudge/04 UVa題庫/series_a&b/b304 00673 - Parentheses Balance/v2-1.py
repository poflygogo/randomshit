for _ in range(int(input())):
    expression = input().rstrip()

    if len(expression) % 2 != 0:
        print('No')
        continue

    for _ in range(64):
        expression = expression.replace('()', '').replace('[]', '')
    
    if expression:
        print('No')
    else:
        print('Yes')
