import random

def generate_expression(depth=3):
    if depth == 0:
        return str(random.randint(1, 9))
    else:
        op = random.choice(('+', '-', '*', '/'))
        left = generate_expression(depth - 1)
        right = generate_expression(depth - 1)
        return f"({left}{op}{right})"

print(generate_expression(4))  # 生成一個深度為4的表達式