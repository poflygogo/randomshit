from sys import stdin

zodiacAF = {
    0:'豬', 1:'鼠', 2:'牛', 3:'虎', 4:'兔', 5:'龍',
    6:'蛇', 7:'馬', 8:'羊', 9:'猴', 10:'雞', 11:'狗'
}
zodiacBE = {
    0:'鼠', 1:'牛', 2:'虎', 3:'兔', 4:'龍', 5:'蛇',
    6:'馬', 7:'羊', 8:'猴', 9:'雞', 10:'狗', 11:'豬'
}


for year in stdin:
    year = int(year)
    print(zodiacAF[year % 12] if year > 0 else zodiacBE[year % 12])