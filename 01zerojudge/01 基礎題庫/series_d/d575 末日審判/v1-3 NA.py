from sys import stdin, stdout


for line in stdin:
    line = [int(i) for i in line.rstrip().split()]
    if abs(line[2] - line[0]) + abs(line[3] - line[1]) > line[4]:
        stdout.write('alive\n')
    else:
        stdout.write('die\n')
