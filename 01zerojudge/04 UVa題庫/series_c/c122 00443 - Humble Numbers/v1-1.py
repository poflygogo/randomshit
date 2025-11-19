# python 3.12
# UVa 00443 Humble Numbers
# ZeroJudge c122


def num_id(n: int) -> str:
    mod = n % 10
    if 11 <= n % 100 <= 13 or not 1 <= mod <= 3:
        return "th"
    if mod == 1:
        return "st"
    if mod == 2:
        return "nd"
    return "rd"


def main():
    humble_numbers = [1]
    p2 = p3 = p5 = p7 = 0
    while n := int(input()):
        while len(humble_numbers) < n:
            next_humble_p2 = humble_numbers[p2] * 2
            next_humble_p3 = humble_numbers[p3] * 3
            next_humble_p5 = humble_numbers[p5] * 5
            next_humble_p7 = humble_numbers[p7] * 7
            humble_numbers.append(
                min(next_humble_p2, next_humble_p3, next_humble_p5, next_humble_p7)
            )
            if humble_numbers[-1] == next_humble_p2:
                p2 += 1
            if humble_numbers[-1] == next_humble_p3:
                p3 += 1
            if humble_numbers[-1] == next_humble_p5:
                p5 += 1
            if humble_numbers[-1] == next_humble_p7:
                p7 += 1
        print(f"The {n}{num_id(n)} humble number is {humble_numbers[n - 1]}.")


main()
