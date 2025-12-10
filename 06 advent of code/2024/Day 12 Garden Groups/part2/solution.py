# advent of code 2025
# Day 12 Garden Groups
# part 1
# python 3.12

import pathlib
from typing import TextIO, NamedTuple
from enum import Enum
from collections import deque
from dataclasses import dataclass
from itertools import product


class Point(NamedTuple):
    row: int
    col: int

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.row + other.row, self.col + other.col)


class Directions(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    RIGHT = Point(0, 1)
    LEFT = Point(0, -1)


@dataclass(slots=True, kw_only=True)
class RegionInfo:
    type: str
    area_size: int
    edge_count: int = 0


class Solution:
    def __init__(self, input_file: TextIO):
        self.graph: list[str] = input_file.read().splitlines()
        self.graph_max_row: int = len(self.graph)
        self.graph_max_col: int = len(self.graph[0])

        # 用來儲存每個座標對應的區域 ID, 0 代表尚未訪問或地圖外的區域
        self.region_map: list[list[int]] = [
            [0] * self.graph_max_col for _ in range(self.graph_max_row)
        ]

        # 儲存每個 ID 的詳細資訊
        self.region_infos: dict[int, RegionInfo] = {}

    def solve(self):
        """入口方法"""
        # 1. 紀錄每個區域的範圍，並標上 id (因為有可能出現相同符號但不屬於同一區的作物)
        curr_id: int = 1
        for r in range(self.graph_max_row):
            for c in range(self.graph_max_col):
                if not self.region_map[r][c]:
                    self.mark_region(Point(r, c), curr_id)
                    curr_id += 1

        # 2. 計算邊緣總數
        self.calc_edges(scan_mode=False)
        self.calc_edges(scan_mode=True)

        # 3. 統計價格
        total_price: int = 0
        for i, info in self.region_infos.items():
            total_price += info.area_size * info.edge_count
        return total_price

    def mark_region(self, point: Point, id: int):
        """標記各區域並統計其面積"""
        # BFS
        queue: deque[Point] = deque([point])
        sign: str = self.graph[point.row][point.col]
        self.region_map[point.row][point.col] = id
        size: int = 1  # 計算面積

        while queue:
            p = queue.popleft()
            for np in map(lambda x: x.value + p, Directions):
                if not self.is_valid_point(np):
                    continue
                if self.graph[np.row][np.col] != sign:
                    continue
                if self.region_map[np.row][np.col] != 0:
                    continue
                queue.append(np)
                self.region_map[np.row][np.col] = id
                size += 1

        # 更新最終結果
        self.region_infos[id] = RegionInfo(type=sign, area_size=size)

    def is_valid_point(self, p: Point) -> bool:
        return 0 <= p.row < self.graph_max_row and 0 <= p.col < self.graph_max_col

    def calc_edges(self, scan_mode: bool = False):
        """掃描 self.region_map 並計算邊數 (Sides)

        主要思路:
        1. 透過掃描每一條 "水平分界線" (currentRow vs previousRow) 來找出水平邊界。
           - 若 scan_mode=True, 則先將矩陣轉置, 將垂直邊界轉換為水平邊界問題處理。
        2. 對於每一個座標點 (r, c), 比較其上方 (id_up) 與下方 (id_dn) 的區域 ID。
           - 若 id_up != id_dn, 表示兩者之間存在邊界。
        3. 判斷邊界連續性 (Side):
           - 不單純計算邊界數量, 而是計算 "連續的邊 (Side)"。
           - 若當前位置 (c) 的邊界是左側 (c-1) 邊界的延伸, 則不計入新邊。
           - 判定為 "新邊 (New Side)" 的條件 (符合任一即可):
             a. 位於最左側 (col=0)。
             b. 左側同側鄰居 (Neighbor Same Side) ID 不同 (表示區域中斷)。
             c. 左側同側鄰居 ID 相同, 但左側位置沒有邊界 (Neighbor Same Side == Neighbor Other Side) (表示轉角或交叉)。

        Args:
            scan_mode(bool): 掃描方式, False 代表計算水平邊(橫線), True 代表計算垂直邊(豎線)
        """
        # 如果是 scan_mode (垂直掃描), 則轉置矩陣，將 "豎線" 視為 "橫線" 處理
        grid = list(zip(*self.region_map)) if scan_mode else self.region_map

        rows: int = len(grid)
        cols: int = len(grid[0])

        def _is_new_side(
            current_id: int,
            col: int,
            neighbor_same_side_id: int,
            neighbor_other_side_id: int,
        ) -> bool:
            """判斷是否為新的邊界起始點

            Args:
                current_id: 當前位置的 ID
                col: 當前 column index
                neighbor_same_side_id: 同側的左邊鄰居 ID (e.g. 若 current_id 是上方 block, 則為左上 block)
                neighbor_other_side_id: 異側的左邊鄰居 ID (e.g. 若 current_id 是上方 block, 則為左下 block)
            """
            if current_id == 0:
                return False

            # 第一行一定是新邊界
            if col == 0:
                return True

            # 左邊鄰居不同區 -> 新邊界
            if neighbor_same_side_id != current_id:
                return True

            # 左邊鄰居同區, 但左邊鄰居的異側也是同區 (說明左邊沒有邊界) -> 新邊界
            if neighbor_same_side_id == neighbor_other_side_id:
                return True

            return False

        # 掃描每一條 "水平" 分界線 (包含 top 0 和 bottom rows)
        for r, c in product(range(rows + 1), range(cols)):
            # 取得分界線上下的 ID (如果是邊界則為 0)
            id_up: int = grid[r - 1][c] if r > 0 else 0
            id_dn: int = grid[r][c] if r < rows else 0

            # 若上下相同，則沒有邊界
            if id_up == id_dn:
                continue

            # 準備左側的 ID (c-1), 若 c=0 則設為 -1
            # (避免與 0 混淆，雖然 0 也是邊界/無效區，但在此邏輯下主要是比對是否相等)
            id_up_prev = (grid[r - 1][c - 1] if r > 0 else 0) if c > 0 else -1
            id_dn_prev = (grid[r][c - 1] if r < rows else 0) if c > 0 else -1

            # 檢查 "上方區域" 的 "下緣" (Bottom Edge)
            # 對於上方區域 (id_up)，同側鄰居是 id_up_prev，異側鄰居是 id_dn_prev
            if _is_new_side(id_up, c, id_up_prev, id_dn_prev):
                self.region_infos[id_up].edge_count += 1

            # 檢查 "下方區域" 的 "上緣" (Top Edge)
            # 對於下方區域 (id_dn)，同側鄰居是 id_dn_prev，異側鄰居是 id_up_prev
            if _is_new_side(id_dn, c, id_dn_prev, id_up_prev):
                self.region_infos[id_dn].edge_count += 1


if __name__ == "__main__":
    test_cases = pathlib.Path(__file__).parent.parent / "test_case"
    for test_case in test_cases.iterdir():
        if test_case.is_file() and test_case.name.endswith(".in"):
            with test_case.open() as f:
                s = Solution(f)
                print(f"{test_case.name}: {s.solve()}")
