for _ in range(int(input())):
    alien_h, alien_m, alien_s = map(int, input().split())
    earth_s = (alien_s + (alien_m + alien_h * 32) * 16) * 4
    print(f'{int(earth_s // 3600)}:{int(earth_s // 60 % 60)}:{int(earth_s % 60)}')