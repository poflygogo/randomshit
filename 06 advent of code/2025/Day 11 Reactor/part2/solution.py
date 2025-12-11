# advent of coed 2025
# Day 11: Reactor
# part 1
# python 3.12

import pathlib
from typing import TextIO
from functools import cache


class Solution:
    START: str = "svr"  # part 2 start
    END: str = "out"
    MUST_CONTAIN: tuple[str, ...] = ("dac", "fft")

    def __init__(self, input_file: TextIO):
        self.graph: dict[str, list[str]]
        self.to_graph(input_file)

    def solve(self) -> int:
        # 雖然 part1 的版本改一改就能直接用，但在 part 2 效率太差了
        # part 1 會遍歷一切路徑，其中絕大部分路徑都是無效的(應該?)，所以需要剪枝
        # 我們只關注會路過 "dac" 和 "fft" 的路徑，那就把路徑拆分成三節計算
        # 這樣就可以避免遍歷那些絕對不可能走的路徑
        @cache
        def count_total_path(start: str, target: str):
            if start == target:
                return 1
            cnt: int = 0
            for i in self.graph.get(start, []):
                cnt += count_total_path(i, target)
            return cnt

        result = (
            count_total_path(self.START, "dac")
            * count_total_path("dac", "fft")
            * count_total_path("fft", self.END)
        )
        result += (
            count_total_path(self.START, "fft")
            * count_total_path("fft", "dac")
            * count_total_path("dac", self.END)
        )

        return result

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
