from sys import stdin


def count_nanb(ans: list, guess: list) -> tuple:
    nA = 0
    for i in range(4):
        if guess[i] == ans[i]:
            nA += 1
            guess[i] = None
            ans[i] = None
    nB = 0
    for num in guess:
        if num != None and num in ans:
            nB += 1
            ans[ans.index(num)] = None
    return nA, nB


for line in stdin:
    if line.strip() == "":
        continue
    password = line.split()

    for _ in range(int(stdin.readline())):
        test = stdin.readline().strip("\r\n").split()
        nA, nB = count_nanb(password.copy(), test)
        print(f"{nA}A{nB}B")
