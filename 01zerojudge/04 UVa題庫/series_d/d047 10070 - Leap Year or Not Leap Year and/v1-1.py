# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10070 Leap Year or Not Leap Year and ...
# Zerojudge d047


def mainloop():
    while True:
        try:
            date = input()
        except EOFError:
            break
        else:
            print(
                *[f'This is {i} year.' for i in gulamatu(int(date))],
                sep='\n'
            )


def gulamatu(year: int) -> list:
    result = []
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        result.append('leap')
        is_leap = True
    
    if year % 15 == 0:
        result.append('huluculu festival')
    
    if is_leap and year % 55 == 0:
        result.append('bulukulu festival')
    
    if result:
        return result
    return ['an ordinary']


if __name__ == '__main__':
    mainloop()
