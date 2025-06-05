from datetime import datetime

def get_datestamp():
    datestamp = datetime.now().strftime('%Y%m%d')
    return datestamp