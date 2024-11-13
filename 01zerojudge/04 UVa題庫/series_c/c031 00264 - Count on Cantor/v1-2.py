from sys import stdin


for num in stdin:
    num = target = int(num.rstrip())

    # 確認在第幾層循環
    stage = 1
    while stage < num:
        num -= stage
        stage += 1

    # 判斷是偶數層還是奇數層
    if stage % 2 == 0:
        value = f'{num}/{stage - num + 1}'
    else:
        value = f'{stage - num + 1}/{num}'

    print(f'TERM {target} IS {value}')
