# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m309. 外星時間


def main():
    for _ in range(int(input())):
        alien_h, alien_m, alien_s = map(int, input().split())
        earth_s = (alien_h * 32 + alien_m) * 16 + alien_s
        earth_s *= 4
        print(
            earth_s // 3600,
            earth_s // 60 % 60,
            earth_s % 60,
            sep=':'
        )


main()
