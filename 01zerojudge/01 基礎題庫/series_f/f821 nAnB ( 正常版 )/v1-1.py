from sys import stdin


answer, query = stdin.readline().rstrip().split()
for _ in range(int(query)):
    guess = stdin.readline().rstrip()

    a, b = 0, 0
    for i in range(len(answer)):
        if guess[i] in answer:
            if guess[i] == answer[i]:
                a += 1
            else:
                b += 1
    print(f'{a}A{b}B')
