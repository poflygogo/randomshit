# python 3.12
# ZeroJudge r858
# TOI 練習賽 新手組 第一題 紅豆餅 (Red Bean Cake)


def solve():
    # [綠豆沙, 紅豆餅1, ... , 紅豆餅5]
    meals = [0] * 6

    input()
    for i in map(int, input().split()):
        meals[i] += 1

    total_red_beam_cake = sum(meals[1:])
    meal_combo = min(total_red_beam_cake, meals[0])
    cost = (
        meal_combo * 59
        + max(0, meals[0] - meal_combo) * 50
        + max(0, total_red_beam_cake - meal_combo) * 20
    )

    print(*meals, cost)


solve()
