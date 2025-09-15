# q671. pC. 歡慶竺呂佰週年校慶
# 114學年度hgsh校內賽

from typing import List

def elevator(n: int, limit_time: int, limit_min: int, limit_max: int, weight_info: List[int]) -> int:
    def is_valid(target_weight: int) -> bool:
        """檢查給定的負載上限是否可以在規定趟數內完成運送"""
        trips = 1
        curr_w = 0
        
        for w in weight_info:
            if w > target_weight:
                return False
            if curr_w + w <= target_weight:
                curr_w += w
            else:
                trips += 1
                curr_w = w
                if trips > limit_time:
                    return False
        return True
    
    left = max(limit_min, max(weight_info))
    right = limit_max
    
    if not is_valid(right):
        return -1
    
    # bfs
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        
        if is_valid(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


def main():
    n, t, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(elevator(n, t, l, r, arr))


if __name__ == '__main__':
    main()

    # import unittest

    # class TestProblem(unittest.TestCase):
    #     def test_sample(self):
    #         test_cases = [
    #             (
    #                 5, 2, 1, 500,
    #                 [60, 80, 60, 70, 50],
    #                 180
    #             ),
    #             (
    #                 5, 2, 300, 500,
    #                 [60, 80, 60, 70, 50],
    #                 300
    #             ),
    #             (
    #                 5, 2, 1, 100,
    #                 [60, 80, 60, 70, 50],
    #                 -1
    #             )
    #         ]
    #         for id, (n, t, l, r, arr, expected) in enumerate(test_cases):
    #             with self.subTest(id):
    #                 self.assertEqual(elevator(n, t, l, r, arr), expected)
    
    # unittest.main()
