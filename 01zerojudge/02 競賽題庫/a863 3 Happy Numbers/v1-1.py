# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a863. 3. Happy Numbers
# HP CodeWars 2010


while True:
    try:
        n = num = int(input())
    except EOFError:
        break
    else:
        temp = set()
        while n not in temp:
            temp.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        
        print(f'{num} is {"a " if n == 1 else "an un"}happy number')
