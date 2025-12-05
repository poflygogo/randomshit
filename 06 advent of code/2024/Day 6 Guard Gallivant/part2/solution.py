# advent of code 2024
# day 6 guard gallivant
# part 2
# python 3.12

import pathlib
from typing import TextIO

from enum import Enum
import bisect


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def next(self) -> "Direction":
        lst: list[Direction] = list(Direction)
        idx: int = lst.index(self)
        next_idx: int = (idx + 1) % len(lst)
        return lst[next_idx]



class Solution:
    def __init__(self, input_file: TextIO):
        self.graph: list[str] = input_file.read().splitlines()
        self.max_row: int = len(self.graph)
        self.max_col: int = len(self.graph[0])
        self.sr, self.sc = self.find_start()
        
        # part2 要處理的資料量大很多，所以要先預處理
        # Precompute obstacles for jump simulation
        self.row_obstacles: list[list[int]] = [[] for _ in range(self.max_row)]
        self.col_obstacles: list[list[int]] = [[] for _ in range(self.max_col)]
        for r, row in enumerate(self.graph):
            for c, char in enumerate(row):
                if char == "#":
                    self.row_obstacles[r].append(c)
                    self.col_obstacles[c].append(r)

    def solve(self) -> int:
        # Get the original path
        path = self.get_path()
        
        candidates_count = 0
        visited_locs = set()
        
        # We need to track visited locations to ensure we only place obstacles
        # on the first encounter of a cell.
        
        for r, c, direction in path:
            visited_locs.add((r, c))
            
            # Determine the cell in front
            dr, dc = direction.value
            nr, nc = r + dr, c + dc
            
            # Check if valid candidate
            if not (0 <= nr < self.max_row and 0 <= nc < self.max_col):
                continue
            if self.graph[nr][nc] == "#":
                continue
            if (nr, nc) == (self.sr, self.sc):
                continue
            if (nr, nc) in visited_locs:
                # If we've been here before, placing an obstacle here would have
                # changed the past path, or we've already checked this candidate.
                continue
                
            # Simulate with obstacle at (nr, nc)
            # Start from current position (r, c) but turned 90 degrees
            # because we hit the new obstacle.
            if self.check_loop_jump((r, c, direction.next()), (nr, nc)):
                candidates_count += 1
                
        return candidates_count

    def find_start(self) -> tuple[int, int]:
        for r, row in enumerate(self.graph):
            if "^" in row:
                return r, row.index("^")
        raise ValueError('Can\'t find "^" from the graph')

    def get_path(self) -> list[tuple[int, int, Direction]]:
        """Returns the full path of the guard as a list of states."""
        path = []
        r, c = self.sr, self.sc
        direction = Direction.UP
        visited = set() # To detect loops in Part 1 (though not expected)
        
        # Add initial state
        path.append((r, c, direction))
        visited.add((r, c, direction))

        while True:
            nr, nc = r + direction.value[0], c + direction.value[1]
            if not (0 <= nr < self.max_row and 0 <= nc < self.max_col):
                break
                
            if self.graph[nr][nc] == "#":
                direction = direction.next()
            else:
                r, c = nr, nc
            
            state = (r, c, direction)
            # In Part 1, we don't expect loops, but good to be safe
            if state in visited:
                break
            visited.add(state)
            path.append(state)
            
        return path

    def check_loop_jump(self, start_state: tuple[int, int, Direction], new_obs: tuple[int, int]) -> bool:
        """
        Checks for a loop using jump simulation.
        start_state: (r, c, dir) - the state just after turning at the new obstacle.
        new_obs: (or, oc) - the position of the temporary obstacle.
        """
        r, c, direction = start_state
        visited_states = {start_state}
        
        # Optimization: track states (r, c, direction) where we turn.
        # Since we jump between obstacles, we only care about states at obstacles.
        
        or_new, oc_new = new_obs
        
        while True:
            # Find the next obstacle in the current direction
            next_r, next_c = -1, -1
            found = False
            
            match direction:
                case Direction.UP:
                    # Look in col_obstacles[c] for max r < current r
                    # Also check new_obs
                    obs_list = self.col_obstacles[c]
                    idx = bisect.bisect_left(obs_list, r)
                    # obs_list[idx] >= r. We want obs_list[idx-1]
                    
                    closest_r = -1
                    if idx > 0:
                        closest_r = obs_list[idx - 1]
                    
                    # Check new obstacle
                    if oc_new == c and or_new < r:
                        if closest_r == -1 or or_new > closest_r:
                            closest_r = or_new
                    
                    if closest_r != -1:
                        next_r, next_c = closest_r + 1, c
                        found = True

                case Direction.DOWN:
                    # Look in col_obstacles[c] for min r > current r
                    obs_list = self.col_obstacles[c]
                    idx = bisect.bisect_right(obs_list, r)
                    # obs_list[idx] > r.
                    
                    closest_r = -1
                    if idx < len(obs_list):
                        closest_r = obs_list[idx]
                    
                    # Check new obstacle
                    if oc_new == c and or_new > r:
                        if closest_r == -1 or or_new < closest_r:
                            closest_r = or_new
                    
                    if closest_r != -1:
                        next_r, next_c = closest_r - 1, c
                        found = True

                case Direction.LEFT:
                    # Look in row_obstacles[r] for max c < current c
                    obs_list = self.row_obstacles[r]
                    idx = bisect.bisect_left(obs_list, c)
                    
                    closest_c = -1
                    if idx > 0:
                        closest_c = obs_list[idx - 1]
                    
                    # Check new obstacle
                    if or_new == r and oc_new < c:
                        if closest_c == -1 or oc_new > closest_c:
                            closest_c = oc_new
                    
                    if closest_c != -1:
                        next_r, next_c = r, closest_c + 1
                        found = True

                case Direction.RIGHT:
                    # Look in row_obstacles[r] for min c > current c
                    obs_list = self.row_obstacles[r]
                    idx = bisect.bisect_right(obs_list, c)
                    
                    closest_c = -1
                    if idx < len(obs_list):
                        closest_c = obs_list[idx]
                    
                    # Check new obstacle
                    if or_new == r and oc_new > c:
                        if closest_c == -1 or oc_new < closest_c:
                            closest_c = or_new
                    
                    if closest_c != -1:
                        next_r, next_c = r, closest_c - 1
                        found = True

            if not found:
                return False # Exited map
            
            # Move to just before obstacle and turn
            r, c = next_r, next_c
            direction = direction.next()
            
            state = (r, c, direction)
            if state in visited_states:
                return True
            visited_states.add(state)


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        s = Solution(input_file)
        print(s.solve())
