from sys import stdin


for _ in range(int(stdin.readline().strip())):
    data = [int(i) for i in stdin.readline().strip().split()]
    
    for i in data:
        if data.count(i) == 2:
            dupl = i
            data.remove(i)
            break
    
    print(
        (max(data) + min(data)) * (len(data) + 1) // 2 - sum(data),
        dupl
    )
