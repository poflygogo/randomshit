# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a882. B. 我灰灰的橡皮鴨是個恐怖的危機
# 102-1 延平資研社第二次練習賽


for _ in range(int(input())):
    data = input().rstrip()
    counter = {'O': 0, 'X': 0, 'H': 0}
    for i in data:
        counter[i] += 1
    print(counter['H'] + counter['X'] * 2)
