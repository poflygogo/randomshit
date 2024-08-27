data = input()
for idx in range(len(data)):
    print(data[idx:]+data[:idx])