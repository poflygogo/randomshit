while True:
    try:text = input().lower()
    except EOFError:break
    check = [i for i in text if i.isalpha()]
    check_set = set(check)
    count_odd = 0
    for i in check_set:
        if check.count(i) % 2 != 0:
            count_odd += 1
    print("yes !") if count_odd <= 1 else print("no...")
