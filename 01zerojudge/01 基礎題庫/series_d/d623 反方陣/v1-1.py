from sys import stdin


for line in stdin:
    line = line.strip().split()
    if line == ['0']: break

    a, b = map(int, line)
    c, d = map(int, next(stdin).strip().split())

    determinant = a * d - b * c
    if determinant == 0:
        print('cheat!')
    
    else:
        print(
            f'{d / determinant: <.5f} {-b / determinant: <.5f}',
            f'{-c / determinant: <.5f} {a / determinant: <.5f}',
            sep='\n'
        )
