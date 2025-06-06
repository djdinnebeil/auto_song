from datetime import datetime

def get_datestamp():
    datestamp = datetime.now().strftime('%Y%m%d')
    return datestamp

def get_military_timestamp():
    military_timestamp = datetime.now().strftime('%H:%M:%S.%f')
    return military_timestamp
