from sys import stdin


class ParkingLot:
    class Car:
        def __init__(self, brand: str, color: str) -> None:
            self.brand = brand
            self.color = color
        
        def __str__(self) -> str:
            return f'{self.brand} {self.color}'

    def __init__(self, total_cars: int) -> None:
        self.parking_lot = self._park(total_cars)

    def _park(self, _n: int) -> list:
        return [ParkingLot.Car(*stdin.readline().rstrip().split()) for _ in range(_n)]
    
    def query(self, total_command: int) -> None:
        for _ in range(total_command):
            command = stdin.readline().rstrip().split()

            if command[0] == 'brand':
                print(*[i for i in self.parking_lot if i.brand == command[1]], sep='\n')
            
            else:
                print(*[i for i in self.parking_lot if i.color == command[1]], sep='\n')
        print()


def main():
    for line in stdin:
        line = line.rstrip()
        if line == '':
            continue

        n, m = map(int, line.split())

        p = ParkingLot(n)
        p.query(m)


if __name__ == '__main__':
    main()
