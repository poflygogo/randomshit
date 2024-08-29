from sys import stdin

zodiac = {
    0:'猴', 1:'雞', 2:'狗', 3:'豬', 4:'鼠', 5:'牛',
    6:'虎', 7:'兔', 8:'龍', 9:'蛇', 10:'馬', 11:'羊'
}

for year in stdin:
    print(zodiac[(int(year) + 1911) % 12])