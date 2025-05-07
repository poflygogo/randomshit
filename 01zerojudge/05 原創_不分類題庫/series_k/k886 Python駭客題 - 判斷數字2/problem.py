import re
from string import digits


def isNumber_Carol(s: str) -> bool:
    return re.match(r'^\d+$', s, re.A) is not None


def isNumber_Dave(s: str) -> bool:
    return bool(s) and all(c in digits for c in s)


def get_result(s):
    print(
        f'<text: {s}>',
        f'C -> {isNumber_Carol(s)}',
        f'D -> {isNumber_Dave(s)}',
        sep='\n'
    )



if __name__ == '__main__':
    test_cases = [
        "123",      # True
        "０１２",   # True（全形數字）
        "123abc",   # False
        "12 34",    # False（包含空格）
        "",         # False（空字符串）
        "١٢٣",      # True（阿拉伯數字）
        '123\n',    # False (帶換行符的字串)
        '123\r',
        '123\r\n',
        '123\u2028',
        '123\u2029'
    ]
    for i in test_cases:
        get_result(i)
