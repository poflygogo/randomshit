from sys import stdin, stdout


stdout.write('\n'.join(str(int(i.rstrip()) - 1) for i in stdin.readlines()))
