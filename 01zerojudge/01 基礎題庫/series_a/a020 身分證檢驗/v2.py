from sys import stdin, stdout

area_dict={
    'A':10,'B':11,'C':23,'D':13,'E':14,
    'F':15,'G':16,'H':17,'I':34,'J':18,
    'K':19,'L':20,'M':21,'N':22,'O':35,
    'P':23,'Q':24,'R':25,'S':26,'T':27,
    'U':28,'V':29,'W':32,'X':30,'Y':31,
    'Z':33
}

id_num = stdin.readline().strip()
id_num = id_num.replace(id_num[0], str(area_dict[id_num[0]]))
total = sum([int(i) * j for i, j in zip(id_num, (1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1))])
if total % 10:
    stdout.write('fake')
else:
    stdout.write('real')