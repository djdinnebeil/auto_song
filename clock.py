from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_time_in_timezone(timezone: str = "UTC"):
    return datetime.now(ZoneInfo(timezone))

def get_current_time():
    return datetime.now()

if __name__ == '__main__':
    print(get_current_time())
    print(get_current_time_in_timezone("America/New_York"))
