from sys import stdin, stdout

ans = stdin.readline()

for _ in range(int(stdin.readline())):
    guess = stdin.readline()

    a = 0
    b = 0
    for idx, item in enumerate(guess[:4]):
        if item in ans:
            if item == ans[idx]:
                a += 1
            else:
                b += 1
    
    stdout.write(f'{a}A{b}B\n')