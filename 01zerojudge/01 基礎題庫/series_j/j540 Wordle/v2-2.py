from sys import stdin, stdout


answer = stdin.readline().rstrip()
counter = {i: answer.count(i) for i in set(answer)}

for _ in range(int(stdin.readline().rstrip())):
    flag = False
    guess_time = 0
    while True:
        guess = stdin.readline().rstrip().rstrip()
        if guess == '#':
            stdout.write('\n')
            break

        if flag:
            continue

        guess_time += 1

        if guess == answer:
            flag = True
            stdout.write(f'OOOOO\nCongradulat1ons ! You guessed {guess_time} times\n')
        elif len(guess) > 5:
            stdout.write('Too long\n')
        elif len(guess) < 5:
            stdout.write('Not enough letters\n')

        else:
            temp_counter = counter.copy()
            result = ['X'] * 5
            for i in range(5):
                if guess[i] == answer[i]:
                    result[i] = 'O'
                    temp_counter[guess[i]] -= 1
                elif guess[i] in answer:
                    result[i] = 'Y'
                    temp_counter[guess[i]] -= 1

            for i in range(4, -1, -1):
                if result[i] != 'Y':
                    continue
                if temp_counter[guess[i]] < 0:
                    result[i] = 'X'
                    temp_counter[guess[i]] += 1

            stdout.write(f'{"".join(result)}\n')
