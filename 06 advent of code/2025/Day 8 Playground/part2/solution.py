# advent of code 2025
# Day 8: Playground
# part 1
# python 3.12

import pathlib
from typing import TextIO, NamedTuple
from itertools import combinations
from dataclasses import dataclass


class Node(NamedTuple):
    x: int
    y: int
    z: int


@dataclass
class Link:
    node1: Node
    node2: Node
    distance: int

    def __gt__(self, other) -> bool:
        if not isinstance(other, Link):
            return NotImplemented
        if self.distance != other.distance:
            return self.distance > other.distance
        else:
            return (self.node1, self.node2) > (other.node1, other.node2)


class Solution:
    def __init__(self, input_file: TextIO):
        self.all_nodes: list[Node] = []
        self.links: list[Link] = []  # max_heap
        self.parents: dict[Node, Node] = {}  # for DSU

        for line in input_file:
            self.all_nodes.append(Node(*map(int, line.split(","))))
        self.find_links()

    def solve(self) -> int:
        # Disjoint Set Union (DSU)
        total_circuits: int = len(self.all_nodes)
        for link in self.links:
            if self.union(link.node1, link.node2):
                total_circuits -= 1
                if total_circuits == 1:
                    return link.node1.x * link.node2.x
        return 0

    # must make a huge list......bruh
    def find_links(self):
        for n1, n2 in combinations(self.all_nodes, 2):
            distance: int = sum((j - i) ** 2 for i, j in zip(n1, n2))
            curr_link: Link = Link(n1, n2, distance)
            self.links.append(curr_link)
        self.links.sort()

    def find(self, x: Node) -> Node:
        if self.parents.get(x, x) == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: Node, y: Node) -> bool:
        root_x: Node = self.find(x)
        root_y: Node = self.find(y)
        if root_x != root_y:
            self.parents[root_x] = root_y
            return True
        return False


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if not input_path.exists():
        print("file not found")
    with input_path.open() as f:
        s = Solution(f)
        print(s.solve())
