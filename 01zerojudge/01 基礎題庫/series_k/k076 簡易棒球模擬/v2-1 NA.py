a, b, c = input().split()
run = input()
if run == '1':
    print(
        sum(i == '1' for i in (a,)),
        f'{b} {c} 1',
        sep='\n'
    )
elif run == '2':
    print(
        sum(i == '1' for i in (a, b)),
        f'{c} 1 0',
        sep='\n'
    )
elif run == '3':
    print(
        sum(i == '1' for i in (a, b, c)),
        '1 0 0',
        sep='\n'
    )
else:
    print(
        sum(i == '1' for i in (a, b, c)) + 1,
        '0 0 0',
        sep='\n'
    )
