from sys import stdin

for line in stdin:
    if line == 0: break

    line = int(line)
    for i in range(line):
        print(f"{'_' * (line - i - 1)}{'+' * (i + 1)}")