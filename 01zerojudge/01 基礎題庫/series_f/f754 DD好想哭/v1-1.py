for case in range(int(input())):
    a, b = map(int, input().split())
    average = a // b
    print(f'Case {case + 1} :')
    [print(f'第{i}位 : 拿{average}元並說DD! BAD!') for i in range(1, b)]
    print(f'第{b}位 : 拿{a - average * (b - 1)}元並說DD! BAD!')
