
from src.date_parser import get_date_range

periods = [
    "this_month",
    "last_month",
    "this_week",
    "next_week",
    "today",
    "all_time",
    "unspecified"
]

for period in periods:
    start_date, end_date = get_date_range(period)

    print(
        f"{period}: {start_date} sampai {end_date}"
    )
