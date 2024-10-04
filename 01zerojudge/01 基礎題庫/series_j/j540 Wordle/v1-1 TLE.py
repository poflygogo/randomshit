answer = input().rstrip()
length = len(answer)
counter = {i: answer.count(i) for i in set(answer)}

for _ in range(int(input())):
    flag = False

    while True:
        guess = input().rstrip()
        if guess == '#':
            print()
            break
        if flag:
            continue

        if guess == answer:
            flag = True
            print(f'{"O" * length}\nCongradulat1ons ! You guessed 1 times')

        elif len(guess) > length:
            print('Too long')

        elif len(guess) < length:
            print('Not enough letters')

        else:
            temp_counter = counter.copy()
            result = []
            for i in range(length):
                if guess[i] == answer[i]:
                    result.append('O')
                    temp_counter[guess[i]] -= 1

                elif guess[i] in answer and temp_counter[guess[i]] > 0:
                    result.append('Y')
                    temp_counter[guess[i]] -= 1

                else:
                    result.append('X')
            print(''.join(result))
