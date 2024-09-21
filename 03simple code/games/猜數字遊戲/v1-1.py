import random


def main():
    ans = random.randint(1, 100)
    for i in range(1, 6):
        print(f'-----第 {i} 次猜測-----')

        while True:
            guess = input('請輸入您猜測的數字 -> ')
            if not guess.isdecimal():
                print(f'請輸入一個正整數，例如: {random.randint(1, 100)}')
                continue
            guess = int(guess)
            if not 0 < guess < 101:
                print('數值超出範圍，請輸入介於 1 - 100 之間的數字')
            else:
                break

        if guess < ans:
            print('不對，猜小了')
        elif guess > ans:
            print('不對，猜大了')
        else:
            print(f'正確!! 你共猜了 {i} 次')
            break
    else:
        print(f'5 次都沒猜中，正確答案是 {ans}')


main()
