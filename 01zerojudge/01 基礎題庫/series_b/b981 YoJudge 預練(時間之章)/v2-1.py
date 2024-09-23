from sys import stdin


for time in stdin:
    time = time.replace(
        "hour", " 3600000 ").replace(
            "h", " 3600000 ").replace(
                "min", " 60000 ").replace(
                    "ms", " 1 ").replace(
                        "m", " 60000 ").replace(
                            "s", " 1000 ").strip().split()
    
    result = sum(float(time[i]) * int(time[i + 1]) for i in range(0, len(time), 2))
    print(f'{result: <.0f}')
    