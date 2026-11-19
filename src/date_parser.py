
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import calendar


TIMEZONE = ZoneInfo("Asia/Jakarta")


def get_date_range(date_period):
    today = datetime.now(TIMEZONE).date()

    if date_period == "this_month":
        start_date = today.replace(day=1)

        last_day = calendar.monthrange(
            today.year,
            today.month
        )[1]

        end_date = today.replace(day=last_day)

    elif date_period == "last_month":
        first_day_this_month = today.replace(day=1)
        end_date = first_day_this_month - timedelta(days=1)
        start_date = end_date.replace(day=1)

    elif date_period == "this_week":
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)

    elif date_period == "next_week":
        start_date = (
            today - timedelta(days=today.weekday())
            + timedelta(days=7)
        )
        end_date = start_date + timedelta(days=6)

    elif date_period == "today":
        start_date = today
        end_date = today

    elif date_period in ["all_time", "unspecified"]:
        return None, None

    else:
        raise ValueError(
            f"Unsupported date period: {date_period}"
        )

    return start_date.isoformat(), end_date.isoformat()
