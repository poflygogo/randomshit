def count_nAnB(ans:str, guess:list) -> int:
    ans = ans.split()
    nA = 0
    for i in range(len(guess)):
        if guess[i] == ans[i]:
            nA += 1
            guess[i] = None
            ans[i] = None

    nB = 0
    for i,num in enumerate(guess):
        if num != None and num in ans:
            nB += 1
    
    return nA, nB

while True:
    try:
        password = input()

        for _ in range(int(input())):
            test = input().split()
            nA, nB = count_nAnB(password, test)
            print(f"{nA}A{nB}B")
    
        input()
    except EOFError:
        break
