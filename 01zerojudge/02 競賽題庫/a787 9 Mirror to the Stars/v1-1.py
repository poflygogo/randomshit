# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a787. 9. Mirror to the Stars
# HP CodeWars 2008


while True:
    try:
        name, col, row, command = input().split()
    
    except EOFError:
        break

    else:
        data = [input() for _ in range(int(row))]
        if command == 'R':
            print(
                name,
                *[line[::-1] for line in data],
                sep='\n'
            )
        
        elif command == 'I':
            print(
                name,
                *data[::-1],
                sep='\n'
            )
        
        else:   # if command == 'IR'
            print(
                name,
                *[line[::-1] for line in data[::-1]],
                sep='\n'
            )
