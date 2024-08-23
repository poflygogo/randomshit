idnum = input()
remain = sum([int(item) * mul for item, mul in zip(idnum, (8, 7, 6, 5, 4, 3, 2, 1, 1))]) % 10

data = ("BNZ","AMW","KLY","JVX","HU","GT","FS","ER","DOQ","CIP")

print(data[(10-remain) % 10])