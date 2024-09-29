num_chr = 'mjqhofawcpnsexdkvgtzblryui'
chr_num = 'uzrmatifxopnhwvbslekycqjgd'

for _ in range(int(input())):
    data = input().split()
    del data[0]

    if data[0].isdecimal():
        print(*[num_chr[int(i) - 1] for i in data], sep='')
    
    else:
        print(sum(chr_num.index(i) + 1 for i in data))
