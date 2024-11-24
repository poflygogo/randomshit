# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a784. 6. PERLs Before Swine
# HP CodeWars 2008


while True:
    try:
        statement = input().rstrip()

    except EOFError:
        break

    else:
        idx = statement.index(' = ')
        statement_part1 = statement[idx:].strip(';')
        statement_part2 = statement[:idx]
        statement_part2 = statement_part2.rsplit(maxsplit=1)
        print(statement_part2[1] + statement_part1, statement_part2[0] + ';')
 