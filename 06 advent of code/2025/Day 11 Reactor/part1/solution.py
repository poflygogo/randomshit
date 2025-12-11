# advent of coed 2025
# Day 11: Reactor
# part 1
# python 3.12

import pathlib
from typing import TextIO
from functools import cache


class Solution:
    START: str = "you"
    END: str = "out"

    def __init__(self, input_file: TextIO):
        self.graph: dict[str, list[str]]
        self.to_graph(input_file)

    def solve(self) -> int:
        @cache
        def dfs(curr_node: str) -> int:
            if curr_node == self.END:
                return 1
            sum_of_path: int = 0
            for next_node in self.graph[curr_node]:
                if next_node in visited:
                    continue
                visited.add(next_node)
                sum_of_path += dfs(next_node)
                visited.remove(next_node)
            return sum_of_path

        visited: set[str] = {self.START}  # 避免出現「環」
        return dfs(self.START)

    def to_graph(self, input_file: TextIO):
        self.graph = {}
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            curr_node, next_nodes = line.split(":")
            self.graph[curr_node] = next_nodes.strip().split()


if __name__ == "__main__":
    test_cases = pathlib.Path(__file__).parent.parent / "test_case"
    for file in test_cases.iterdir():
        if not file.is_file():
            continue
        if not file.name.endswith(".in"):
            continue
        with file.open() as f:
            s = Solution(f)
            print(f"{file.name}: {s.solve()}")
