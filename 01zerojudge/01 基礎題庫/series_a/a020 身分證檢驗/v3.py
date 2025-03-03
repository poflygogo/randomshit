def is_valid_id_num(id_num: str) -> bool:
    if id_num[1] not in ('1', '2'):
        return False

    weight = (1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1)
    area_id={
        'A':10,'B':11,'C':23,'D':13,'E':14,
        'F':15,'G':16,'H':17,'I':34,'J':18,
        'K':19,'L':20,'M':21,'N':22,'O':35,
        'P':23,'Q':24,'R':25,'S':26,'T':27,
        'U':28,'V':29,'W':32,'X':30,'Y':31,
        'Z':33
    }

    id_num = id_num.replace(id_num[0], str(area_id[id_num[0]]))
    return sum(int(id_num[i]) * weight[i] for i in range(11)) % 10 == 0


id_num = input()
if is_valid_id_num(id_num):
    print('real')
else:
    print('fake')
