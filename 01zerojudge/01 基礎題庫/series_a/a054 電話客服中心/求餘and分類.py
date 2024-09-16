area_dict={
    'A':10,'B':11,'C':23,'D':13,'E':14,
    'F':15,'G':16,'H':17,'I':34,'J':18,
    'K':19,'L':20,'M':21,'N':22,'O':35,
    'P':23,'Q':24,'R':25,'S':26,'T':27,
    'U':28,'V':29,'W':32,'X':30,'Y':31,
    'Z':33
}

# 取key
area = list(area_dict.keys())

# 取餘
remain = [(area_dict[item] // 10 + area_dict[item] % 10 * 9) % 10 for item in area_dict]

# 合併後根據餘數大小排列
sort = sorted(list(zip(area, remain)), key= lambda x: x[1])

print(f'根據餘數增冪排序結果:\n{sort}')