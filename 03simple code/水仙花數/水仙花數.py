for i in range(100, 1000):
    if i == sum(int(j) ** 3 for j in str(i)):
        print(i)
