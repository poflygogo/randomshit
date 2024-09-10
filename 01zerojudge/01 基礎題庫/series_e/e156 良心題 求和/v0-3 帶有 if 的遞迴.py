def get_ans(n :int) -> int:
    if n == 1:
        return 1
    return n + get_ans(n - 1)

print(get_ans(int(input())))