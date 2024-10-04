from sys import stdin, stdout


for _ in range(int(stdin.readline().rstrip())):
    stdout.write('請使用配方法解下列一元二次方程式\n\n')

    for i in range(int(stdin.readline().rstrip())):
        a, b, c = map(int, stdin.readline().rstrip().split())
        output = [f'{a if a != 1 else ""}x^2']
        if b != 0:
            output.append(f'{b if b != 1 else "":+}x')
        if c != 0:
            output.append(f'{c:+}')

        stdout.write(f'{i + 1}. {"".join(output)}=0\n\n')
    stdout.write('考試要加油口屋')
