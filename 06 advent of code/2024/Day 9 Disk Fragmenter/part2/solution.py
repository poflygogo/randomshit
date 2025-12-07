# advent of code 2024
# day 9 disk fragmenter
# part 2
# python 3.12

import pathlib
from typing import TextIO, Optional
from dataclasses import dataclass


@dataclass
class Segment:
    val: int | None
    size: int


class Solution:
    def __init__(self, input_file: TextIO):
        self.segments: list[Segment] = []

        flag: bool = True
        curr_val: int = 0

        for i in map(int, input_file.read().strip()):
            if flag:
                self.segments.append(Segment(val=curr_val, size=i))
                curr_val += 1
            elif i > 0:
                self.segments.append(Segment(val=None, size=i))
            flag = not flag

        self.max_val: int = curr_val - 1

    def solve(self) -> int:
        for curr_id in range(self.max_val, -1, -1):
            # find the right segment
            rgt = self._find_match_segment(val=curr_id)
            if rgt == -1:
                continue
            rgt_seg: Segment = self.segments[rgt]

            # find the left segment
            lft: int = self._find_match_segment(val=None, min_size=rgt_seg.size, end_index=rgt)
            
            if lft == -1:
                continue
                
            lft_seg: Segment = self.segments[lft]

            # merge the right segment into the left segment
            remain_space: int = lft_seg.size - rgt_seg.size
            lft_seg.val = rgt_seg.val
            lft_seg.size = rgt_seg.size
            rgt_seg.val = None

            # if there is remaining space, create a new segment
            if remain_space > 0:
                self.segments.insert(lft + 1, Segment(val=None, size=remain_space))
                rgt += 1

            # merge the segments
            if rgt + 1 < len(self.segments) and self.segments[rgt + 1].val is None:
                self.segments[rgt].size += self.segments[rgt + 1].size
                self.segments.pop(rgt + 1)
            
            if rgt - 1 >= 0 and self.segments[rgt - 1].val is None:
                self.segments[rgt - 1].size += self.segments[rgt].size
                self.segments.pop(rgt)

        return self._calculate_checksum()

    def _calculate_checksum(self) -> int:
        result: int = 0
        pos: int = 0
        for seg in self.segments:
            if seg.val is not None:
                start = pos
                end = pos + seg.size - 1

                # equal to sum(range(start, end + 1))
                segment_sum = seg.size * (start + end) // 2

                result += seg.val * segment_sum
            pos += seg.size
        return result

    def _find_match_segment(self, val: Optional[int] = None, min_size: int = 0, end_index: int = -1) -> int:
        """
        Find the first segment that matches the given value and has at least min_size.
        If val matches, it returns the index.

        args:
            val(int | None): the value to search for
            min_size(int): the minimum size of the segment
            end_index(int): the index to stop searching at
        """
        limit = len(self.segments) if end_index == -1 else end_index
        for i in range(limit):
            seg = self.segments[i]
            if seg.val != val:
                continue
            if seg.size < min_size:
                continue
            return i
        return -1


if __name__ == "__main__":
    test_cases_name: list[str] = [
        "00.in",  # main test case
        "01.in",  # sample test case
    ]
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"

    if input_path.exists():
        with input_path.open() as input_file:
            s = Solution(input_file)
            print(s.solve())
