mystr = input()
mylist = list()
for x in mystr:
    mylist.append(chr(ord(x) - 7))
a = str(mylist).replace('\', \'','').strip('\'[]')
print(a)
