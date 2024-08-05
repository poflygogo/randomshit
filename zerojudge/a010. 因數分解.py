
# 輸入
num = int(input())

# 定義空列表
quality_list = list()

# 設定因數為2(最小的質數)
quality = 2

# 質因數分解，將結果添加到 quality_list
while num != quality:
    if num % quality == 0:
        quality_list.append(quality)
        num /= quality
    else:
        quality += 1
quality_list.append(quality)

# 去重 排序
quality_list_clean = sorted(list(set(quality_list)))

for n in quality_list_clean:
    if quality_list_clean.index(n)+1 != len(quality_list_clean):
        if quality_list.count(n) == 1:
            print('%d *'%(n),end=' ')
        else:
            print('%d^%d *'%(n,quality_list.count(n)),end=' ')
    else:
        if quality_list.count(n) == 1:
            print('%d '%(n))
        else:
            print('%d^%d '%(n,quality_list.count(n)))
