# 根據題目格式，將所有資料放到同一個 list 中
# 最後把放在最後的 0 移除
numbers = [int(i) for i in input().split()]
while numbers[-1] != 0:
    numbers.extend(int(i) for i in input().split())
del numbers[-1]

# 輸出開頭字串
print('PERFECTION OUTPUT')

# 逐一處理每個數字
for num in numbers:
    # 紀錄因數
    factors = {1, num}
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            factors.update({n, num // n})
    factors.remove(num)

    # 判斷該輸出 PERFECT, DEFICIENT, 或 ABUNDANT
    factors_total = sum(factors)
    if num == factors_total:
        print(f'{num:>5d}  PERFECT')
    elif num > factors_total:
        print(f'{num:>5d}  DEFICIENT')
    else:
        print(f'{num:>5d}  ABUNDANT')

# 輸出結尾
print('END OF OUTPUT')
