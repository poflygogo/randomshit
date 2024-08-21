# 用map()執行capitalize()方法
print(
    *map(lambda x: x.capitalize(), input().split()),
    sep='\n'
)