# q671. pC. 歡慶竺呂佰週年校慶
# 114學年度hgsh校內賽


from typing import List

def elevator(n: int, limit_time: int, limit_min: int, limit_max: int, weight_info: List[int]) -> int:
    def is_valid(target_weight: int) -> bool:
        t = 0
        curr_w = 0
        for w in weight_info:
            if curr_w + w <= target_weight:
                curr_w += w
            else:
                curr_w = w
                t += 1
                if t > limit_time:
                    return False
        return t < limit_time

    for target_weight in range(max(limit_min, max(weight_info)), limit_max + 1):
        if is_valid(target_weight):
            return target_weight
    return -1


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
