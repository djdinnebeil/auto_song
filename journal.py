from datetime import datetime

def get_datestamp():
    datestamp = datetime.now().strftime('%Y%m%d')
    return datestamp

def get_military_timestamp():
    military_timestamp = datetime.now().strftime('%H:%M:%S.%f')
    return military_timestamp

def get_am_pm_timestamp():
    am_pm_timestamp = datetime.now().strftime('%I:%M %p')
    if am_pm_timestamp[0] == '0':
        am_pm_timestamp = am_pm_timestamp[1:]
    return am_pm_timestamp

def get_episode_title(title):
    title = f'{title}\n'
    title += f'Entry {get_datestamp()}\n'
    title += f'{get_military_timestamp()}\n\n'
    title += f'{get_am_pm_timestamp()}'
    return title