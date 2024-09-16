while True:
    try:
        num_in = int(input())
    except:
        break
    num_out = ''
    while num_in != 0:
        remain = num_in % 2
        num_in = num_in // 2
        num_out += str(remain)
    print(num_out[::-1])
