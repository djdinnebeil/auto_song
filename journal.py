from datetime import datetime
import clipboard
import pygetwindow as gw

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

def print_to_screen(self, message):
    print(message)
    clipboard.copy_to_clipboard(f'{message}\n\n')
    clipboard.paste_from_clipboard()

def format_song(self, song=None, artist=None, album=None):
    return f'[{song}] [{artist}] [{album}]'

# def save_word_document(self):
#     active_window_title = gw.getActiveWindow().title
#     if active_window_title[:len('Document')] == 'Document':
#         keyboard.save_document()