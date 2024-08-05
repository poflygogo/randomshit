
area_dict={
    'A':10,'B':11,'C':23,'D':13,'E':14,
    'F':15,'G':16,'H':17,'I':34,'J':18,
    'K':19,'L':20,'M':21,'N':22,'O':35,
    'P':23,'Q':24,'R':25,'S':26,'T':27,
    'U':28,'V':29,'W':32,'X':30,'Y':31,
    'Z':33
}

id_num = input()
id_num = id_num.replace(id_num[0],str(area_dict[id_num[0]]))

index = 1
n = 0
for multiplier in range(9,0,-1):
    n += int(id_num[index]) * multiplier
    index += 1
n += int(id_num[0]) + int(id_num[-1])

if n % 10 == 0:print('real')
else:print('fake')
