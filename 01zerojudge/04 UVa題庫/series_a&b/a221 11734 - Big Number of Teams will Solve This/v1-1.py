from sys import stdin


for i in range(1, int(stdin.readline().rstrip()) + 1):
    submit = next(stdin).rstrip()
    judge = next(stdin).rstrip()

    print(
        f'Case {i}:',
        'Yes' if submit == judge else
        'Output Format Error' if submit.replace(' ', '') == judge else
        'Wrong Answer'
    )
