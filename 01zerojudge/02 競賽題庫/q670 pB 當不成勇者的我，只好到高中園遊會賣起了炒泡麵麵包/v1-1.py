# q670. pB. 當不成勇者的我，只好到高中園遊會賣起了炒泡麵麵包
# 114學年度hgsh校內賽

# Greedy
# 目標是在確保炒麵麵包在生產過程中，美味度絕對不會低於 0
# 那樣我們只需要優先讓「可以提高美味度的人」先處理
# 最後才讓那些會出包的人碰，就可以盡可能確保美味度都維持正數了

from typing import List, Tuple

def yakisoba_bread(n: int, arr: List[int]) -> Tuple[int, List[int]]:
    greater, lesser = [], []
    for i in arr:
        if i >= 0:
            greater.append(i)
        else:
            lesser.append(i)
    res_n = max(0, -sum(arr))
    return res_n, greater + lesser


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    res_n, res_arr = yakisoba_bread(n, arr)
    print(res_n)
    print(*res_arr)


if __name__ == '__main__':
    main()

    # import unittest

    # def checker(n: int, arr: list[int]) -> bool:
    #     for i in arr:
    #         n += i
    #         if n < 0:
    #             return False
    #     return True


    # class TestProblem(unittest.TestCase):
    #     def test_sample(self):
    #         test_cases = [
    #             (
    #                 5,
    #                 [3, -3, -1, 1, 2],
    #                 0,
    #                 [3, -3, 1, -1, 2]
    #             )
    #         ]
    #         for id, (n, arr, expect_n, expect_arr) in enumerate(test_cases):
    #             with self.subTest(f"test case: {id}"):
    #                 res_n, res_arr = yakisoba_bread(n, arr)
    #                 self.assertEqual(res_n, expect_n, f"{expect_n=}, got={res_n}")
    #                 self.assertTrue(checker(res_n, res_arr), f"sample output={expect_arr}")
    
    # unittest.main()
