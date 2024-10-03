import random


def main():
    ans = random.randint(1, 10000000)

    guess_time = 0
    while True:
        get_input = input().split()     # 輸入格式應為: 指令 數字，如: r 225
        if not get_input:
            continue

        match get_input[0]:
            case 'r':   # request
                print(1 if int(get_input[1]) >= ans else 0)
                guess_time += 1

            case 'u':   # upload_answer
                print(
                    'AC' if int(get_input[1]) == ans else 'WA',
                    f'The answer is {ans}.',
                    f'Your answer is: {int(get_input[1])}.',
                    f'request: {guess_time} times.',
                    sep='\n'
                )
                break

            case _:
                print('Valid command, please re-try')


if __name__ == '__main__':
    main()

# python 3.12
# @poflygogo 2024-10-03
# 應該...沒寫錯邏輯吧
