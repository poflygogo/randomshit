# python 3.12
# UVa 477 Points in Figures: Rectangles and Circles
# ZeroJudge d093

from typing import NamedTuple


class Circle(NamedTuple):
    x: float
    y: float
    r: float


class Square(NamedTuple):
    x1: float
    x2: float
    y1: float
    y2: float


class Point(NamedTuple):
    x: float
    y: float


def main():
    figures = []
    while (line := input().strip().split()) and line != ["*"]:
        if line[0] == "c":
            figures.append(Circle(*map(float, line[1:])))
        else:  # line[0] == "r"
            x1, y1, x2, y2 = map(float, line[1:])
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            figures.append(Square(x1, x2, y1, y2))

    test_case = 1
    while (p := Point(*map(float, input().split()))) and not (p.x == p.y == 9999.9):
        is_contained = False
        for i, f in enumerate(figures, start=1):
            if isinstance(f, Circle) and ((p.x - f.x) ** 2 + (p.y - f.y) ** 2) < f.r**2:
                print(f"Point {test_case} is contained in figure {i}")
                is_contained = True
            elif isinstance(f, Square) and (f.x1 < p.x < f.x2) and (f.y1 < p.y < f.y2):
                print(f"Point {test_case} is contained in figure {i}")
                is_contained = True
        if not is_contained:
            print(f"Point {test_case} is not contained in any figure")
        test_case += 1


main()
