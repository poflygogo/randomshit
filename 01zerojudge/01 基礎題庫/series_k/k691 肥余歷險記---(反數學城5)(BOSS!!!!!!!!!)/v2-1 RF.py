import math


for _ in range(int(input())):
    data = input()
    if 'sqrt' in data:
        _, a = data.split()
        print(int(math.sqrt(int(a))))
    else:
        print(eval(data))