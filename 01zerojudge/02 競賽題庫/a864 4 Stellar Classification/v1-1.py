# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a864. 4. Stellar Classification
# HP CodeWars 2010


while True:
    star_data = input().split()
    if star_data[0] == 'END':
        break
    BV_color = float(star_data[1]) - float(star_data[2])

    if BV_color < -0.25:
        spectral_class = 'O'
    elif BV_color < 0:
        spectral_class = 'B'
    elif BV_color < 0.25:
        spectral_class = 'A'
    elif BV_color < 0.5:
        spectral_class = 'F'
    elif BV_color < 1:
        spectral_class = 'G'
    elif BV_color < 1.5:
        spectral_class = 'K'
    else:
        spectral_class = 'M'
    
    print(f'{star_data[0]} {BV_color:.2f} {spectral_class}')
