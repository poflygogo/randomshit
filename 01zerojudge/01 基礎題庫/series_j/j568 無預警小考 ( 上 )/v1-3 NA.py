from sys import stdin


for _ in range(int(stdin.readline().rstrip())):
    print('請使用配方法解下列一元二次方程式', end='\n\n')

    for i in range(int(stdin.readline().rstrip())):
        a, b, c = map(int, stdin.readline().rstrip().split())
        output = [f'{a if a != 1 else ""}x^2']
        if b != 0:
            if b == 1:
                output.append(f'+x')
            else:
                output.append(f'{b:+}x')
        if c != 0:
            output.append(f'{c:+}')

        print(f'{i + 1}. {"".join(output)}=0', end='\n\n')
    print('考試要加油口屋')
