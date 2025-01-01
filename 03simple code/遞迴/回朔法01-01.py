# -*- encoding: utf-8 -*-
# python 3.12

# 窮舉 n 位數密碼的所有可能(數字 1 到 3)


def create_password(max_depth: int, password: list[int], depth: int=0) -> list[int]:
    if depth == max_depth:
        print(password)
        return
    for i in range(3):
        password.append(i + 1)
        create_password(max_depth, password, depth + 1)
        password.pop()


if __name__ == '__main__':
    n = 3
    create_password(n, [])
