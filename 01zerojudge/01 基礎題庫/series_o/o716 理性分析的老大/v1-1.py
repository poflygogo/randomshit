print(
    str(round((lambda x, y: x * (1 + y))(*map(float, input().split())), 1)).rstrip('0').rstrip('.')
)

# zerojudge o716
# 題目未公開
# AC (19ms, 3.3MB)
# 2024-10-22
