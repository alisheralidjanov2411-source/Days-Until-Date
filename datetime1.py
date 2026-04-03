from datetime import datetime

today =datetime.now()
print(f"Сегодня: {today.strftime('%d-%m-%Y %H:%M')}")

target_date =datetime(2026, 11, 24)
days_left = target_date - today

print(f"До 24 ноября 2026 года осталось {days_left.days} дней.")