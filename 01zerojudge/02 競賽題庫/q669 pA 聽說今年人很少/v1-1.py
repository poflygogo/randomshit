# ZeroJudge q669. pA. 聽說今年人很少
# 114學年度hgsh校內賽
# python 3.12


from typing import NamedTuple, List, Literal
from itertools import groupby

# Literal 是 python 3.8 以後才有的功能，zerojudge 只有到 python 3.6(2025-09-15)
# 如果想在 python 3.6 執行，請把 Literal 相關的語句移除即可，基本邏輯不變 
Result = Literal["Top 5", "Maybe Top 5", "Top 10", "Thank You"]

class ScoreInfo(NamedTuple):
    score: int
    id: int

def check_my_rank(n: int, scores: List[ScoreInfo]) -> str:
    my_score = scores[0].score
    scores.sort(key=lambda x: (-x.score, x.id))
    if scores[0] == my_score:
        return "Top 5"
    rank = 0
    for score, detail in groupby(scores, key=lambda x: x.score):
        if score == my_score:
            if rank > 5:
                return "Top 10"
            if rank + len(list(detail)) > 5:
                return "Maybe Top 5"
            else:
                return "Top 5"
        rank += len(list(detail))
        if rank > 10:
            break
    return "Thank You"


def main():
    n = int(input())
    arr = [ScoreInfo(int(input()), i) for i in range(n)]
    print(check_my_rank(n, arr))


if __name__ == "__main__":
    main()

    # import unittest

    # class TestFunction(unittest.TestCase):
    #     def test_sample(self):
    #         test_cases: list[tuple[int, list[int], Result]] = [
    #             (
    #                 15,
    #                 [90,70,50,30,90,70,60,90,90,30,10,20,70,30,30],
    #                 "Top 5"
    #             ),
    #             (
    #                 15,
    #                 [70,30,50,30,90,70,60,90,90,90,10,20,70,30,30],
    #                 "Maybe Top 5"
    #             ),
    #             (
    #                 15,
    #                 [30,70,50,30,90,70,60,90,90,90,10,20,70,30,30],
    #                 "Top 10"
    #             ),
    #             (
    #                 15,
    #                 [20,70,50,30,90,70,60,90,90,90,10,30,70,30,30],
    #                 "Thank You"
    #             ),
    #             (
    #                 15,
    #                 [90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0],
    #                 "Maybe Top 5"
    #             ),
    #             (
    #                 15,
    #                 [90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0],
    #                 "Top 5"
    #             )
    #         ]
    #         for id, (n, arr, expected) in enumerate(test_cases):
    #             with self.subTest(f"test case {id}, {expected=}"):
    #                 arr = [ScoreInfo(j, i) for i, j in enumerate(arr)]
    #                 self.assertEqual(t := check_my_rank(n, arr), expected, f"{expected=}, got=\'{t}\'")

    # unittest.main()
