from datetime import timedelta, datetime

print(
    (datetime.strptime(input(), '%H %M') + timedelta(hours=2, minutes=30)).strftime('%H:%M')
)