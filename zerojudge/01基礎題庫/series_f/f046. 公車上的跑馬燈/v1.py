width:int = int(input())
data:str = input()
target:int = int(input())

data:str = (' ' * width) + data + (' ' * width)
print(data[target:target+width])