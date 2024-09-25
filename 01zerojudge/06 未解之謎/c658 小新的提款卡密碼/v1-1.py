from sys import stdin


def is_possible_square(n: int) -> bool:
    """判斷該數的每一位數字重新排列組合後是否有可能成為完全平方數"""
    def set_interection(n: str):
        return bool({'1', '4', '5', '6', '9'}.intersection(set(n)))

    def digit_sum(n: int) -> bool:
        while n > 9:
            n = sum(int(i) for i in str(n))
        return n in (1, 4, 7, 9)
    
    def mod_3_and_4(n: int) -> bool:
        return (n % 3 in (0, 1)) or (n % 4 in (0, 1))
    
    return set_interection(str(n)) or digit_sum(n) or mod_3_and_4(n)


def is_square(n: int) -> bool:
    """精準判斷一個數字是否為完全平方數"""
    return (n ** 0.5).is_integer()


for num in stdin:
    num = num.strip()

    # 初篩，把一些明顯不可能湊成完全平方數的組合篩掉
    if not is_possible_square(int(num)):
        print(0)

    else:
        # 紀錄元素數量，把數字打散
        counter = {}
        for i in num:
            counter[i] = counter.get(i, 0) + 1

        # 後面沒頭緒了
        # 應該要先挑一個數字，且該數在 (1, 4, 5, 6, 9) 的範圍中，把這個數字放到個位數
        # 然後對剩下的數字做排列組合......嗎?
        # 感覺有點瘋狂
