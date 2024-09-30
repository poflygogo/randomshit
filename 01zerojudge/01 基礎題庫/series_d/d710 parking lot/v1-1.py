from sys import stdin


class Car:
    def __init__(self, brand: str, color: str) -> None:
        self.brand = brand
        self.color = color
    
    def __str__(self) -> str:
        return f'{self.brand} {self.color}'


for line in stdin:
    line = line.rstrip()
    if line == '':
        continue

    cars, coms = map(int, line.split())
    data = [Car(*stdin.readline().rstrip().split()) for _ in range(cars)]

    for _ in range(coms):
        command = stdin.readline().rstrip().split()

        if command[0] == 'brand':
            print(*[i for i in data if i.brand == command[1]], sep='\n')
        
        else:
            print(*[i for i in data if i.color == command[1]], sep='\n')
    
    print()
