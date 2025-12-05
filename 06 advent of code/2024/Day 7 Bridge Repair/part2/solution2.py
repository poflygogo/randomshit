# advent of code 2024
# day 7 bridge repair
# part 2
# python 3.12

import pathlib
from typing import TextIO

class Solution:
    def __init__(self, input_file: TextIO):
        self.input_file: TextIO = input_file

    def solve(self) -> int:
        result: int = 0
        for line in self.input_file:
            if not line.strip():
                continue
            target, nums = self.parse_line(line)
            if self.is_possible(target, nums):
                result += target
        return result

    def parse_line(self, line: str) -> tuple[int, list[int]]:
        target_str, nums_str = line.strip().split(":")
        return int(target_str), list(map(int, nums_str.strip().split()))

    def is_possible(self, target: int, nums: list[int]) -> bool:
        """
        Check if the target can be reached using +, *, || operators.
        Optimized using reverse search (meet-in-the-middle / backtracking from end).
        """
        
        def backtrack(curr_target: int, idx: int) -> bool:
            # Base case: if we are at the first number, it must match the current target
            if idx == 0:
                return curr_target == nums[0]
            
            last = nums[idx]
            
            # 1. Try undoing Addition (+)
            # If the last operation was +, then curr_target = prev + last
            # So prev = curr_target - last
            # We require prev >= 0 (assuming non-negative numbers)
            if curr_target >= last:
                if backtrack(curr_target - last, idx - 1):
                    return True
            
            # 2. Try undoing Multiplication (*)
            # If the last operation was *, then curr_target = prev * last
            # So prev = curr_target / last
            # We require curr_target to be divisible by last
            if last != 0:
                if curr_target % last == 0:
                    if backtrack(curr_target // last, idx - 1):
                        return True
            else:
                # If last is 0, multiplication results in 0.
                # So if curr_target is 0, it's a match (we found a valid path ending in * 0)
                if curr_target == 0:
                    return True

            # 3. Try undoing Concatenation (||)
            # If the last operation was ||, then curr_target ends with digits of last
            # We calculate the power of 10 that covers 'last' to split it
            tens = 10
            while tens <= last:
                tens *= 10
            
            # Check if curr_target ends with last
            if curr_target % tens == last:
                # Ensure we are not just matching the number itself (unless prefix is 0)
                # e.g. 5 || 5 -> 55. 5 is suffix. prev is 5.
                # e.g. 0 || 5 -> 5. 5 is suffix. prev is 0.
                # curr_target // tens gives the prefix
                if backtrack(curr_target // tens, idx - 1):
                    return True
            
            return False

        return backtrack(target, len(nums) - 1)

if __name__ == "__main__":
    # Adjust path to point to the test_case directory as per user setup
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_path.exists():
        with input_path.open() as input_file:
            s = Solution(input_file)
            print(s.solve())
    else:
        print(f"Input file not found: {input_path}")
