from sys import stdin

celestial = {
    0:'庚', 1:'辛', 2:'壬', 3:'癸', 4:'甲',
    5:'乙', 6:'丙', 7:'丁', 8:'戊', 9:'己'
}

terrestrial = {
    0:'申', 1:'酉', 2:'戌', 3:'亥', 4:'子', 5:'丑',
    6:'寅', 7:'卯', 8:'辰', 9:'巳', 10:'午', 11:'未'
}

for year in stdin:
    year = int(year)
    print(
        f'{celestial[year % 10]}{terrestrial[year % 12]}'
    )