# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k722. 肥余歷險記---(數學城3)


result_yu = "�ΧE"  # 這到底是三小??? 不應該是"肥余"嗎??? 編碼問題請好好處理行嗎??
result_li = "肥李"
result_eq = "打平"

choices = {"A": 0, "B": 1, "C": 2}
score = [0, 0]
while True:
    try:
        a, b = input(), input()
        if a == b:
            continue
        score[(choices[a] - choices[b]) % 3 - 1] += 1
    except EOFError:
        break

print(*score, sep="\n")
print(
    result_eq
    if score[0] == score[1]
    else result_yu
    if score[0] > score[1]
    else result_li
)
