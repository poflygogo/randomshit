for i in range(1, int(input()) + 1):
    data = [int(i) for i in input().split()]
    data.sort()
    if data[0] + data[1] > data[2]:
        if data[0] == data[1] == data[2]:
            print(f'Case {i}: Equilateral')
        elif data[0] == data[1] or data[1] == data[2]:
            print(f'Case {i}: Isosceles')
        else:
            print(f'Case {i}: Scalene')
    else:
        print(f'Case {i}: Invalid')
