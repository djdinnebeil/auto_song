from datetime import datetime
from zoneinfo import ZoneInfo
import config

def get_current_time_in_timezone(timezone: str = "UTC"):
    return datetime.now(ZoneInfo(timezone))

def get_current_time():
    return datetime.now()

def get_formatted_date():
    return datetime.today().strftime("%#m-%#d-%y")

def get_local_time_dict():
    now = datetime.now()
    return {
        'year': now.year,
        'month': now.month,
        'day': now.day,
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second,
        'millisecond': int(now.microsecond / 1000)
    }

def format_minutes(minutes: int):
    if minutes < 10:
        return f'0{minutes}'
    return f'{minutes}'

def format_hour(hour: int):
    if hour < config.end_of_day:
        hour += 24
    elif hour < 10:
        return f'0{hour}'
    elif 13 <= hour < 22:
        hour -= 12
    return f'{hour}'

if __name__ == '__main__':
    print(get_current_time())
    print(get_current_time_in_timezone("America/New_York"))
    print(get_formatted_date())
    print(get_local_time_dict()['hour'])
    print(format_minutes(datetime.now().minute))
    print(format_hour(datetime.now().hour))