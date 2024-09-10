import math
import re


for _ in range(int(input())):
    data = input()
    if 'sqrt' in data:
        _, a = data.split()
        print(int(math.sqrt(int(a))))
    else:
        a, e, b = re.findall(r'\d+|\D+', data)
        if e == '+':
            print(int(a) + int(b))
        elif e == '-':
            print(int(a) - int(b))
        elif e == '*':
            print(int(a) * int(b))
        elif e == '/':
            print(int(a) // int(b))
        else:
            print(pow(int(a), int(b)))
