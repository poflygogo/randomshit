hh, mm = map(int, input().split())
mm += (hh * 60 + 150) % 1440
print(f'{mm // 60 :02d}:{mm % 60 :02d}')