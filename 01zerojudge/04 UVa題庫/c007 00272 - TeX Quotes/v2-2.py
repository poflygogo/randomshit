from sys import stdin, stdout


data = stdin.read()
flag = True
for i in data:
    if i == '"':
        if flag:
            stdout.write('``')
        else:
            stdout.write('\'\'')
        flag = not flag

    else:
        stdout.write(i)
