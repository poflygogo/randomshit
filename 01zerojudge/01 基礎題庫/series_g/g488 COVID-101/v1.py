def covid101(num:int) -> int:
    if num == 1:
        return 1
    return covid101(num - 1) + num ** 2 - num + 1

print(covid101(int(input())))