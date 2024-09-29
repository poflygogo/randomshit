from sys import stdin, stdout


for line in stdin:
    line = line.rstrip().split()
    if abs(int(line[2]) - int(line[0])) + abs(int(line[3]) - int(line[1])) > int(line[4]):
        stdout.write('alive\n')
    else:
        stdout.write('die\n')
