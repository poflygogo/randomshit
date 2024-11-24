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
        idx = statement.index('(')
        stack = 1
        for i in range(idx + 1, len(statement)):
            if statement[i] == '(':
                stack += 1
            
            elif statement[i] == ')':
                stack -= 1
                if stack == 0:
                    idx_split = i + 2
                    break
        
        print(statement[idx_split:].strip(';') + ' ' + statement[:idx_split - 1] + ';')
