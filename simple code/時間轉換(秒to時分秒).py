def convert_sec_HMS(second:int) -> tuple:
    out_sec = int(second % 60)
    out_min = int(second // 60 % 60)
    out_hour = int(second // 3600)
    return out_hour, out_min, out_sec


time_in_sec = 100
time = convert_sec_HMS(time_in_sec)
print(f'時間是{time[0]}小時{time[1]}分{time[2]}秒')