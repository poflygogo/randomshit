def my_sort_rule(char:str) -> int:
    a, b = map(int, char.split())
    return a ** 2 + b ** 2

data = [input() for _ in range(int(input()))]
data.sort(key= my_sort_rule)
print(data[-2])