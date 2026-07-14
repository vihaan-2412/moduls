import datetime

months = [datetime.date(2026, month, 1).strftime("%B") for month in range(1, 13)]
for month_name in months:
    print(month_name)
