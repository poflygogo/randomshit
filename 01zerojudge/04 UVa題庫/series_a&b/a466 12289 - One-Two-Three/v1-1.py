for _ in range(int(input())):
    word = input().rstrip()
    if len(word) > 3:
        print(3)

    elif sum(word[i] == 'one'[i] for i in range(3)) >= 2:
        print(1)

    else:
        print(2)
