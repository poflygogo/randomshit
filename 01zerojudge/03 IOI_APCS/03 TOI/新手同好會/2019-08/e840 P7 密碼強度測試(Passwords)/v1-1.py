# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e840 P7 密碼強度測試(Passwords)
# 2019-08 TOI 新手同好會


def password_strength(s: str) -> int:
    length = len(s)
    alpha = digit = consecutive_digit = 0
    for i in range(length):
        if s[i].isalpha():
            alpha += 1
        if s[i].isdigit():
            digit += 1
            if i > 0 and s[i - 1].isdigit():
                consecutive_digit += 1
    
    score = length * 3 + (-5 if length < 8 or alpha == 0 or digit == 0 else 10)
    score += alpha * 3 + digit * 2
    score -= alpha * (alpha == length) + digit * (digit == length)
    score -= consecutive_digit * 2
    return score


if __name__ == '__main__':
    print(password_strength(input()))

    # test = [
    #     '123456',
    #     'Q8e8e8QaPpLe',
    #     '2020Happy2000'
    # ]
    # ans = [9, 79, 68]
    # for t, a in zip(test, ans):
    #     assert password_strength(t) == a, f'case: \'{t}\' -> {password_strength(t)} != {a}'
