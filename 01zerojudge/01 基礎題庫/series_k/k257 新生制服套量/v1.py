data = input()
print(data[0] + f'{"0"*(4 - len(data))}' + data[1:])