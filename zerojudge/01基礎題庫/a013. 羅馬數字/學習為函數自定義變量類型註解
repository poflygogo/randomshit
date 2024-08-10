def rome_to_num(rome:str):
    """
    羅馬數字轉阿拉伯數字
    :param rome: 羅馬數字
    :return: 十進制數字
    """
    rome_dict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000}
    outnum = rome_dict[rome[0]]
    for index in range(1,len(rome)):
        if rome_dict[rome[index]] <= rome_dict[rome[index-1]]:
            outnum += rome_dict[rome[index]]
        else:
            outnum = outnum - rome_dict[rome[index-1]] * 2 + rome_dict[rome[index]]
    return outnum

def num_to_rome(num:int):
    """
    阿拉伯數字轉羅馬數字
    :param convertTOnum: 十進制數字
    :return: 羅馬數字
    """
    rome_tuple = (
        (1,'I'), (4,'IV'), (5, 'V'), (9, 'IX'),
        (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'),
        (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'),
        (1000, 'M')
    )
    outrome = str()
    index = 12
    while index >= 0:
        while num >= rome_tuple[index][0]:
            outrome += rome_tuple[index][1]
            num -= rome_tuple[index][0]
        index -= 1
    return outrome


while True:
    """
    當測資輸入到最後面的"#"時，其實是給了"#\r"
    所以要用rstrip()方法將\r去掉
    """
    rome = input().rstrip()
    if rome == '#':
        break
    else:
        rome_num = tuple(map(rome_to_num,rome.split()))
        diff = abs(rome_num[0] - rome_num[1])
        if diff == 0:
            print('ZERO')
        else:
            print(num_to_rome(diff))
