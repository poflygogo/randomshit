from  sys import  stdin, stdout

for i in range(int(stdin.readline().strip())):
    a, b, c = map(int, stdin.readline().strip().split())

    data = [str(i) for i in range(a + 1, b) if i % c]
    if data:
        f = ' '.join(data) + '\n'
        stdout.write(f)
    else:
        stdout.write('No free parking spaces.\n')