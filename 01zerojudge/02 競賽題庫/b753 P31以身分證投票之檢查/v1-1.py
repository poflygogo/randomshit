# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b753. P31以身分證投票之檢查
# 101學年度商業類程式設計競賽正式題


from sys import stdin
scan = stdin.readline


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


def main():
    for n in stdin:
        if not n.rstrip():
            continue

        duplicate = 0
        invalid = 0
        valid_id = set()
        invalid_id = set()
        for _ in range(int(n.rstrip())):
            id_num = scan().rstrip()
            if id_num in valid_id:
                duplicate += 1
                continue
            elif id_num in invalid_id:
                invalid += 1
                continue
            if is_valid_id_num(id_num):
                valid_id.add(id_num)
            else:
                invalid_id.add(id_num)
                invalid += 1
        
        print(len(valid_id), duplicate, invalid, sep=',')


if __name__ == '__main__':
    main()
