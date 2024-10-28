from sys import stdin


for num in stdin:
    num = int(num.rstrip())

    # 確認在第幾層循環
    stage = 1
    while stage * (stage + 1) // 2 < num:
        stage += 1

    # 求等差數列和
    pre_digit = stage * (stage - 1) // 2

    # 判斷是偶數層還是奇數層
    if stage % 2 == 0:
        value = f'{(num - pre_digit)}/{stage - (num - pre_digit) + 1}'
    else:
        value = f'{stage - (num - pre_digit) + 1}/{(num - pre_digit)}'

    print(f'TERM {num} IS {value}')
