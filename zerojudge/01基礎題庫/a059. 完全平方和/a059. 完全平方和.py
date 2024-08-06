for t in range(int(input())):
    count = 0
    for n in range(int(input()),int(input())):
        if n ** 0.5 % 1 == 0:
            count += n
    print(f"Case {t+1}: {count}")
