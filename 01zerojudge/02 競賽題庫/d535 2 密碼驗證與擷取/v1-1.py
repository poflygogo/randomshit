# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d535. 2. 密碼驗證與擷取
# 98學年度北基區資訊學科能力競賽


def code_checker(code: str) -> bool:
    if not 10 <= len(code) <= 30:
        return False
    if not code.isdigit():
        return False
    if code != code[::-1]:
        return False    
    iterator = map(int, code)
    prev = next(iterator)
    for i in iterator:
        if i > prev * 2:
            return False
        prev = i
    return True


def get_ans(code: str) -> str:
    return ''.join(str(i) for i in map(int, code) if i % 2 == 0) or "0"


def main():
    code = input().strip()
    if code_checker(code):
        print(get_ans(code))
    else:
        print("INCORRECT")


main()
