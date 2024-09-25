for _ in range(int(input())):
    data = [int(i) for i in input().split()]
    
    for i in data:
        if data.count(i) == 2:
            dupl = i
            data.remove(i)
            break
    
    print(
        (max(data) + min(data)) * (len(data) + 1) // 2 - sum(data),
        dupl
    )
