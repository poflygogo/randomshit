import random


def request(n: int) -> bool:
    global guess_time
    guess_time += 1
    return n >= ans


def upload_answer(n: int):
    if n == ans:
        if guess_time <= 30:
            print(
                f'答案正確，但搜尋次數過多。您猜了 {guess_time} 次',
                f'您的答案為：{n}',
                f'正確答案為：{ans}',
                sep='\n'
            )

        else:
            print(
                f'AC\n您共猜了 {guess_time} 次'
            )

    else:
        print(
            '您的答案比對不符合。',
            f'您的答案為：{n}',
            '正確答案為：不告訴你',
            sep='\n'
        )


ans = random.randint(1, 10000000)
guess_time = 0


if __name__ == '__main__':
    pass
