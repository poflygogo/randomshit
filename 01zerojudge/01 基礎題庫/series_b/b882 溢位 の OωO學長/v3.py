hr, mi, sec = map(int, input().split())

# 86400 = 60 * 60 * 24
sec = (hr * 3600 + mi * 60 + sec) % 86400

print(f'{sec//3600:02d}:{sec // 60 % 60:02d}:{sec % 60:02d}')