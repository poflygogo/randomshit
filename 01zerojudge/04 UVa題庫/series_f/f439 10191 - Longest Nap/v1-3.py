# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10191 Longest Nap
# ZeroJudge f439


def mainloop():
    day = 0
    while True:
        try:
            times_busy = get_time_data()
        except EOFError:
            break
        else:
            day += 1
            if times_busy:
                times_busy = merge_time(times_busy)
                times_free = get_free_times(times_busy)
                time, duration = get_ans(times_free)
                print(f'Day #{day}: the longest nap starts at {time} and will last for {duration} minutes.')
            else:
                print(f'Day #{day}: the longest nap starts at 10:00 and will last for 8 hours and 0 minutes.')


def get_time_data() -> list:
    """接收資料，並將資料初步處理"""
    s = int(input())
    result = set()
    for _ in range(s):
        a, b, _ = input().split(maxsplit=2)
        a1, a2 = map(int, a.split(':'))
        b1, b2 = map(int, b.split(':'))
        result.add((a1 * 60 + a2, b1 * 60 + b2))
    return sorted(result)


def merge_time(times: list) -> list:
    # 合併時間，將重疊或相連的時間串接起來
    result = [times.pop(0)]
    for a, b in times:
        if a > result[-1][1]:
            result.append((a, b))
        elif b > result[-1][1]: # and result[-1][0] <= a <= result[-1][1]
            result.append((result.pop()[0], b))
    return result


def get_free_times(times: list) -> list:
    # (start(min), duration(min))
    result = []
    if times[0][0] > 600:
        result.append((600, times[0][0] - 600))
    for i in range(len(times) - 1):
        result.append((times[i][1], times[i + 1][0] - times[i][1]))
    if times[-1][1] < 1080:
        result.append((times[-1][1], 1080 - times[-1][1]))
    return result


def get_ans(times: list) -> tuple:
    time, duration = max(times, key=lambda x: (x[1], -x[0]))
    return (
        f'{time // 60}:{time % 60:02d}',
        str(duration) if duration < 60 else f'{duration // 60} hours and {duration % 60}'
    )


mainloop()
