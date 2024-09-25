for _ in range(int(input())):
    data = sorted(map(int, input().split()))
    
    for i in data:
        if data.count(i) == 2:
            dupl = i
            data.remove(i)
            break
    
    print(
        (data[0] + data[-1]) * (len(data) + 1) // 2 - sum(data),
        dupl
    )
